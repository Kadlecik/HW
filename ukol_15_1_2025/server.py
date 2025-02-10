import socket
import threading

class NoughtsAndCrossesServer:
    def __init__(self, host='127.0.0.1', port=65432):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((host, port))
        self.server_socket.listen(2)
        print(f"Server listening on {host}:{port}")
        self.players = []
        self.board = [' ']*9
        self.current_turn = 0

    def handle_player(self, conn, addr):
        print(f"Player connected from {addr}")
        conn.sendall(b"Welcome to Noughts and Crosses! Waiting for another player...\n")
        self.players.append(conn)
        if len(self.players) == 2:
            self.start_game()

    def start_game(self):
        for player in self.players:
            player.sendall(b"The game is starting!\n")
        self.players[0].sendall(b"You are X. Your turn!\n")
        self.players[1].sendall(b"You are O. Wait for your turn...\n")

    def process_move(self, move, player_index):
        if move not in ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]:
            return b"Invalid move. Try again.\n"
        index = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"].index(move)
        if self.board[index] != ' ':
            return b"Cell already taken. Try again.\n"
        self.board[index] = 'X' if player_index == 0 else 'O'
        self.current_turn = 1 - self.current_turn
        return b"Move accepted.\n"

    def handle_moves(self, conn, player_index):
        while True:
            move = conn.recv(1024).decode().strip()
            if move:
                result = self.process_move(move, player_index)
                conn.sendall(result)
                if b"Move accepted.\n" in result:
                    self.update_board()

    def update_board(self):
        board_state = f"""
        {self.board[0]} | {self.board[1]} | {self.board[2]}
        ---------
        {self.board[3]} | {self.board[4]} | {self.board[5]}
        ---------
        {self.board[6]} | {self.board[7]} | {self.board[8]}
        """
        for player in self.players:
            player.sendall(board_state.encode())
        if self.current_turn == 0:
            self.players[0].sendall(b"You are X. Your turn!\n")
            self.players[1].sendall(b"Wait for your turn...\n")
        else:
            self.players[0].sendall(b"Wait for your turn...\n")
            self.players[1].sendall(b"You are O. Your turn!\n")

    def run(self):
        while True:
            conn, addr = self.server_socket.accept()
            thread = threading.Thread(target=self.handle_player, args=(conn, addr))
            thread.start()
            if len(self.players) == 2:
                threading.Thread(target=self.handle_moves, args=(self.players[0], 0)).start()
                threading.Thread(target=self.handle_moves, args=(self.players[1], 1)).start()

if __name__ == "__main__":
    server = NoughtsAndCrossesServer()
    server.run()
