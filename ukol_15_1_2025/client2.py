import socket

class NoughtsAndCrossesClient:
    def __init__(self, host='127.0.0.1', port=65432):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((host, port))
        self.run()

    def run(self):
        while True:
            message = self.client_socket.recv(1024).decode()
            if message:
                print(message)
                if "Your turn!" in message:
                    move = input("Enter your move (e.g., A1, B2): ")
                    self.client_socket.sendall(move.encode())
            else:
                break

if __name__ == "__main__":
    client = NoughtsAndCrossesClient()
