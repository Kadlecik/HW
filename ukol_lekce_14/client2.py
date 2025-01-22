import socket
import threading
import random
import time

class TicTacToeClient2:
    def __init__(self, host='127.0.0.1', port=65432):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((host, port))
        print("Connected to server")
        self.player = None
        self.board = [' '] * 9  # Inicializace prázdné desky
        threading.Thread(target=self.receive_messages, daemon=True).start()

    def receive_messages(self):
        while True:
            try:
                message = self.client_socket.recv(1024).decode()
                if not message:
                    print("Connection closed by server.")
                    break

                print(f"Server: {message}")

                if "Game starting! Player" in message:
                    self.player = 'X' if "Player 1" in message else 'O'
                    print(f"Assigned as player {self.player}")

                elif "wins" in message or "draw" in message or "loses" in message:
                    print("Game over!")
                    break

                elif "Your move" in message:
                    if f"Player {self.player}" in message:  # Automat je na tahu, pokud odpovídá hráč
                        print("Automat je na tahu...")
                        self.make_move()

                elif "|" in message:  # Zpráva obsahuje desku
                    self.update_board(message)

            except Exception as e:
                print(f"Error receiving message: {e}")
                break

    def send_message(self, message):
        self.client_socket.send(message.encode())
        print(f"Sent message: {message}")

    def make_move(self):
        time.sleep(1)  # Simulace zpoždění při rozhodování
        move = random.choice([i for i in range(9) if self.board[i] == ' '])  # Náhodný volný tah
        print(f"Automat vybral tah {move}")
        self.send_message(str(move))

    def update_board(self, message):
        try:
            lines = message.split("\n")
            new_board = []
            for line in lines:
                if "|" in line:  # Zpracování řádku desky
                    symbols = [symbol.strip() for symbol in line.split("|")]
                    new_board.extend(symbols)
            if len(new_board) == 9:
                self.board = new_board
            print(f"Aktualizovaný stav desky: {self.board}")
        except Exception as e:
            print(f"Error updating board: {e}")

    def run(self):
        print("Waiting for the game to start...")
        while True:
            time.sleep(0.1)  # Udržování běhu klienta

if __name__ == "__main__":
    client = TicTacToeClient2()
    client.run()
