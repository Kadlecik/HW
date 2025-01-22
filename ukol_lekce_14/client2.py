import socket
import threading
import random
import time

class TicTacToeClient2:
    def __init__(self, host='127.0.0.1', port=65435):
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

                # Určení, zda je automat hráčem X nebo O
                if "Game starting! Player" in message:
                    self.player = 'X' if "Player 1" in message else 'O'
                    print(f"Assigned as player {self.player}")

                # Konec hry
                elif "wins" in message or "draw" in message or "loses" in message:
                    print("Game over!")
                    break

                # Výzva k tahu
                elif "Your move" in message and f"Player {self.player}" in message:
                    print("Automat je na tahu...")
                    self.make_move()

                # Aktualizace desky
                elif "Board" in message:
                    self.update_board(message)

            except Exception as e:
                print(f"Error receiving message: {e}")
                break

    def send_message(self, message):
        self.client_socket.send(message.encode())
        print(f"Sent message: {message}")

    def make_move(self):
        time.sleep(1)  # Simulace zpoždění při rozhodování
        try:
            # Najdi volné pozice na desce
            available_moves = [i for i in range(9) if self.board[i] == ' ']
            print(f"Volné tahy: {available_moves}")
            if available_moves:
                move = random.choice(available_moves)  # Vyber náhodný tah
                print(f"Automat vybral tah {move}")
                self.send_message(str(move))
            else:
                print("Žádné volné tahy!")
        except Exception as e:
            print(f"Error making move: {e}")

    def update_board(self, message):
        try:
            # Extrahuje obsah desky z přijaté zprávy
            lines = [line.strip() for line in message.split("\n") if "|" in line]
            new_board = []
            for line in lines:
                symbols = line.split("|")
                for symbol in symbols:
                    new_board.append(symbol.strip() if symbol.strip() in ['X', 'O'] else ' ')
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
