import socket
import threading

class TicTacToeClient1:
    def __init__(self, host='127.0.0.1', port=65435):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((host, port))
        print("Connected to server")
        self.player = None
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
            except Exception as e:
                print(f"Error receiving message: {e}")
                break

    def send_message(self, message):
        self.client_socket.send(message.encode())
        print(f"Sent message: {message}")

    def run(self):
        while self.player is None:
            pass  # Čekání na přiřazení hráče

        while True:
            message = input("Zadej svůj tah (0-8) nebo napiš 'stop' pro ukončení hry: ")
            self.send_message(message)
            if message.lower() == 'stop':
                break

if __name__ == '__main__':
    client = TicTacToeClient1()
    client.run()
