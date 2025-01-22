import socket
import threading
import random
import time

class TicTacToeClient2:
    def __init__(self, host='127.0.0.1', port=65440):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((host, port))
        print("Connected to server")
        self.player = None
        threading.Thread(target=self.receive_messages, daemon=True).start()

    def receive_messages(self):
        while True:
            try:
                message = self.client_socket.recv(1024).decode()
                if not message:
                    print("Connection closed by server.")
                    break

                print(f"Server: {message}")

                if "You are player" in message:
                    self.player = message.split()[-1]

                elif "Your move" in message:
                    self.make_move()
            except Exception as e:
                print(f"Error receiving message: {e}")
                break

    def make_move(self):
        time.sleep(1)
        move = random.choice([i for i in range(9)])
        self.client_socket.send(str(move).encode())

    def run(self):
        print("Client 2 is running...")
        while True:
            pass

if __name__ == '__main__':
    client = TicTacToeClient2()
    client.run()
