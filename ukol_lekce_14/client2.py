import socket
import threading
import random
import time

class TicTacToeClient2:
    def __init__(self, host='127.0.0.1', port=65450):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((host, port))
        print("Connected to server")
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
                    print(f"Assigned as player {self.player}")
                elif "wins" in message or "draw" in message or "loses" in message:
                    print("Konec hry!")
                    break
                elif "Board" in message:
                    print("Aktualizace desky...")
                    self.update_board(message.split('\n')[1:4])  # Aktualizace desky se třemi řádky
                    print("Deska aktualizována:", self.board)
                    if self.player == 'O':
                        print("Automat je na tahu...")
                        self.make_move()  # Automat udělá tah po aktualizaci desky
            except Exception as e:
                print(f"Error receiving message: {e}")
                break

    def send_message(self, message):
        self.client_socket.send(message.encode())
        print(f"Sent message: {message}")

    def make_move(self):
        time.sleep(1)  # Čekání 1 sekundu před tahem
        move = random.choice([i for i in range(9) if self.board[i] == ' '])  # Výběr náhodného tahu z volných polí
        print(f"Automat vybral tah {move}")
        self.send_message(str(move))

    def run(self):
        while self.player is None:
            time.sleep(0.1)  # Čekání na přiřazení hráče

    def update_board(self, board_lines):
        try:
            new_board = []
            for line in board_lines:
                print(f"Processing line: {line}")  # Ladicí výstup pro zpracování řádků desky
                if '|' in line:
                    # Rozdělit řádek podle '|'
                    symbols = line.split('|')
                    print(f"Symbols extracted: {symbols}")  # Ladicí výstup pro extrahované symboly
                    # Odstranit případné mezery a přidat symboly do board_mapping
                    for symbol in symbols:
                        s = symbol.strip()
                        if s in ['X', 'O']:
                            new_board.append(s)
                        else:
                            new_board.append(' ')
            if len(new_board) == 9:
                self.board = new_board
            print(f"Aktualizovaný stav desky: {self.board}")
        except Exception as e:
            print(f"Chyba při aktualizaci desky: {e}")

if __name__ == "__main__":
    client = TicTacToeClient2()
    client.run()
