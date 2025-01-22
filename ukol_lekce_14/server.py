import socket
import threading

class TicTacToeServer:
    def __init__(self, host='127.0.0.1', port=65450):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((host, port))
        self.server_socket.listen(2)
        self.clients = []
        self.board = [' '] * 9
        self.current_player = 0
        self.game_over = False

    def handle_client(self, client_socket, player_id):
        try:
            print(f"Player {player_id} connected")
            client_socket.send(f'You are player {player_id}'.encode())
            while not self.game_over:
                if self.current_player + 1 == player_id:  # Kontrola, jestli je na tahu tento hráč
                    self.send_to_client(client_socket, self.format_board())
                    self.send_to_client(client_socket, f"Your move, Player {player_id} (0-8 or 'stop'): ")

                    message = client_socket.recv(1024).decode().strip()
                    if not message:
                        print(f"Player {player_id} disconnected.")
                        break

                    print(f"Received from Player {player_id}: {message}")

                    if message.lower() == 'stop':
                        self.game_over = True
                        self.send_to_all(f'Player {player_id} has stopped the game. Player {player_id} loses!')
                        break

                    elif message.isdigit():
                        move = int(message)
                        if 0 <= move < 9 and self.board[move] == ' ':
                            self.board[move] = 'X' if player_id == 1 else 'O'
                            if self.check_winner():
                                self.send_to_all(self.format_board())
                                self.send_to_all(f'Player {player_id} wins!')
                                self.game_over = True
                            elif ' ' not in self.board:
                                self.send_to_all(self.format_board())
                                self.send_to_all('Draw!')
                                self.game_over = True
                            self.current_player = 1 - self.current_player
                        else:
                            self.send_to_client(client_socket, 'Invalid move. Try again.')
                    else:
                        self.send_to_client(client_socket, 'Invalid input. Please enter a number between 0-8 or "stop".')
                else:
                    threading.Event().wait(0.1)  # Pokud není tento hráč na tahu, čeká
        except Exception as e:
            print(f"Error with player {player_id}: {e}")
        finally:
            print(f"Closing connection for Player {player_id}")
            client_socket.close()

    def send_to_all(self, message):
        for client in self.clients:
            try:
                client.send(message.encode())
            except Exception as e:
                print(f"Error sending to client: {e}")

    def send_to_client(self, client_socket, message):
        try:
            client_socket.send(message.encode())
        except Exception as e:
            print(f"Error sending to client: {e}")

    def format_board(self):
        return f'\nBoard:\n {self.board[0]} | {self.board[1]} | {self.board[2]}\n-+-+-\n {self.board[3]} | {self.board[4]} | {self.board[5]}\n-+-+-\n {self.board[6]} | {self.board[7]} | {self.board[8]}'

    def check_winner(self):
        winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != ' ':
                return True
        return False

    def start(self):
        print('Server is running...')
        while len(self.clients) < 2:
            try:
                client_socket, _ = self.server_socket.accept()
                self.clients.append(client_socket)
                player_id = len(self.clients)
                threading.Thread(target=self.handle_client, args=(client_socket, player_id), daemon=True).start()
            except Exception as e:
                print(f"Error accepting client: {e}")

if __name__ == '__main__':
    server = TicTacToeServer()
    server.start()
