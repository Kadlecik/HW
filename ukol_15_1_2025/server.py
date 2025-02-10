import socket
import threading


class TicTacToeServer:
    def __init__(self, host='127.0.0.1', port=65432):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Allow reuse of the address
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((host, port))
        self.server_socket.listen(2)
        print(f"Server listening on {host}:{port}")
        self.players = []  # List of player sockets
        self.board = [' '] * 9  # Game board (9 cells)
        self.current_turn = 0  # 0 = first player, 1 = second player
        self.game_active = False  # Indicates if the game is active
        self.lock = threading.Lock()  # To synchronize access to shared resources
        self.player_threads = []  # List to hold player move threads

    def handle_player(self, conn, addr):
        print(f"Player connected from {addr}")
        conn.sendall(b"Welcome to Tic Tac Toe!\n")
        with self.lock:
            if len(self.players) == 0:
                # First player connected
                self.players.append(conn)
                conn.sendall(b"Waiting for a second player...\n")
            elif len(self.players) == 1:
                # Second player: ask for confirmation
                conn.sendall(
                    b"Do you accept the invitation to play? Type 'YES' to accept, or anything else to decline: ")
                response = conn.recv(1024).decode().strip().upper()
                if response == "YES":
                    self.players.append(conn)
                    conn.sendall(b"Game is starting!\n")
                    try:
                        self.players[0].sendall(b"The second player accepted. Game is starting!\n")
                    except:
                        pass
                    # Set up the game and assign symbols
                    self.game_active = True
                    self.players[0].sendall(b"You are 'X'. Your turn!\n")
                    self.players[1].sendall(b"You are 'O'. Wait for your turn...\n")
                    # Start threads for handling moves
                    t0 = threading.Thread(target=self.handle_moves, args=(self.players[0], 0))
                    t1 = threading.Thread(target=self.handle_moves, args=(self.players[1], 1))
                    t0.start()
                    t1.start()
                    self.player_threads.extend([t0, t1])
                else:
                    conn.sendall(b"Game declined. Closing connection.\n")
                    conn.close()
                    # Inform the first player
                    try:
                        self.players[0].sendall(b"The second player declined the game. Closing connection.\n")
                        self.players[0].close()
                    except:
                        pass
                    self.players = []
            else:
                # If a game is already in progress, reject additional connections.
                conn.sendall(b"A game is already in progress. Please try again later.\n")
                conn.close()

    def process_move(self, move, player_index):
        if not self.game_active:
            return b"Game is not active.\n"
        # Check if the correct player is making the move
        if player_index != self.current_turn:
            return b"It's not your turn. Please wait for your turn.\n"
        valid_moves = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
        if move.upper() not in valid_moves:
            return b"Invalid move. Try again.\n"
        index = valid_moves.index(move.upper())
        with self.lock:
            if self.board[index] != ' ':
                return b"This cell is already taken. Try again.\n"
            # Set the player's symbol
            symbol = 'X' if player_index == 0 else 'O'
            self.board[index] = symbol
            # Check if someone has won
            winner = self.check_winner()
            if winner:
                self.game_active = False
                self.update_board()
                self.send_to_all(f"Player '{winner}' wins!\n".encode())
                self.ask_rematch()
                return b""
            elif ' ' not in self.board:
                # It's a draw
                self.game_active = False
                self.update_board()
                self.send_to_all(b"It's a draw!\n")
                self.ask_rematch()
                return b""
            # Switch turn to the other player
            self.current_turn = 1 - self.current_turn
        return b"Move accepted.\n"

    def handle_moves(self, conn, player_index):
        while self.game_active:
            try:
                move = conn.recv(1024).decode().strip()
                if not move:
                    break
                if move.upper() == "STOP":
                    with self.lock:
                        if self.game_active:
                            self.game_active = False
                            loser = 'X' if player_index == 0 else 'O'
                            winner = 'O' if player_index == 0 else 'X'
                            self.send_to_all(
                                f"Player '{loser}' stopped the game and loses. Player '{winner}' wins!\n".encode())
                            self.ask_rematch()
                    break
                else:
                    result = self.process_move(move, player_index)
                    if result:
                        try:
                            conn.sendall(result)
                        except:
                            pass
                        # If the move was accepted, update the board and send turn notifications
                        if b"Move accepted." in result:
                            self.update_board()
            except Exception as e:
                print("Error processing move:", e)
                break

    def update_board(self):
        board_state = "\n"
        board_state += f" {self.board[0]} | {self.board[1]} | {self.board[2]} \n"
        board_state += "---+---+---\n"
        board_state += f" {self.board[3]} | {self.board[4]} | {self.board[5]} \n"
        board_state += "---+---+---\n"
        board_state += f" {self.board[6]} | {self.board[7]} | {self.board[8]} \n"
        self.send_to_all(board_state.encode())

        # Send turn notifications if the game is still active
        if self.game_active:
            if self.current_turn == 0:
                try:
                    self.players[0].sendall(b"Your turn ('X').\n")
                    self.players[1].sendall(b"Wait for your turn ('O').\n")
                except:
                    pass
            else:
                try:
                    self.players[0].sendall(b"Wait for your turn ('X').\n")
                    self.players[1].sendall(b"Your turn ('O').\n")
                except:
                    pass

    def send_to_all(self, message):
        for player in self.players:
            try:
                player.sendall(message)
            except Exception as e:
                print("Error sending message:", e)

    def check_winner(self):
        b = self.board
        win_conditions = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
            (0, 4, 8), (2, 4, 6)  # diagonals
        ]
        for (i, j, k) in win_conditions:
            if b[i] == b[j] == b[k] and b[i] != ' ':
                return b[i]
        return None

    def ask_rematch(self):
        # Ask both players if they want a rematch
        self.send_to_all(b"Do you want a rematch? Type 'REMATCH' for a new game or 'EXIT' to quit: ")
        responses = []
        for player in self.players:
            try:
                response = player.recv(1024).decode().strip().upper()
                responses.append(response)
            except:
                responses.append("EXIT")
        if all(resp == "REMATCH" for resp in responses):
            # Reset the game
            with self.lock:
                self.board = [' '] * 9
                self.current_turn = 0
                self.game_active = True
            self.send_to_all(b"Starting a new game!\n")
            self.players[0].sendall(b"You are 'X'. Your turn!\n")
            self.players[1].sendall(b"You are 'O'. Wait for your turn...\n")
            # Start new threads for handling moves
            t0 = threading.Thread(target=self.handle_moves, args=(self.players[0], 0))
            t1 = threading.Thread(target=self.handle_moves, args=(self.players[1], 1))
            t0.start()
            t1.start()
            self.player_threads = [t0, t1]
        else:
            self.send_to_all(b"Game over. Thanks for playing!\n")
            for player in self.players:
                try:
                    player.close()
                except:
                    pass
            self.players = []
            self.game_active = False

    def run(self):
        while True:
            conn, addr = self.server_socket.accept()
            threading.Thread(target=self.handle_player, args=(conn, addr)).start()


if __name__ == "__main__":
    server = TicTacToeServer()
    server.run()
