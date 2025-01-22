import socket
import threading
import random
import time

class TicTacToeClient2:
    def __init__(self, host='localhost', port=12346):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((host, port))
        self.player = None
        self.board = [' '] * 9  # Inicializace prázdné desky
        threading.Thread(target=self.receive_messages).start()

    def receive_messages(self):
        while True:
            try:
                message = self.client_socket.recv(1024).decode()
                print(f"Server: {message}")
                if "You are player" in message:
                    self.player = message.split()[-1]
                elif "wins" in message or "draw" in message or "loses" in message:
                    print("Konec hry!")
                    break
                elif "Board" in message:
                    print("Aktualizace desky...")
                    self.update_board(message.split('\n')[1:])  # Aktualizace desky
                    print("Deska aktualizována:", self.board)
            except Exception as e:
                print(f"Error receiving message: {e}")
                break

    def send_message(self, message):
        self.client_socket.send(message.encode())

    def run(self):
        while self.player is None:
            time.sleep(0.1)  # Čekání na přiřazení hráče

        while True:
            if self.player == 'O':
                time.sleep(1)  # Čekání 1 sekundu před tahem
                move = random.choice([i for i in range(9) if self.board[i] == ' '])  # Výběr náhodného tahu z volných polí
                print(f"Automat vybral tah {move}")
                self.send_message(str(move))
            else:
                message = input("Zadej svůj tah (0-8) nebo napiš 'stop' pro ukončení hry: ")
                print(f"Odesílání: {message}")
                self.send_message(message)
                if message.lower() == 'stop':
                    break

    def update_board(self, board_lines):
        for i, line in enumerate(board_lines):
            self.board[i] = line.strip()

if __name__ == "__main__":
    client = TicTacToeClient2()
    client.run()
