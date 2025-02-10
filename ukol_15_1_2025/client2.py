import socket

class TicTacToeClient:
    def __init__(self, host='127.0.0.1', port=65432):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((host, port))
        self.run()

    def run(self):
        while True:
            try:
                message = self.client_socket.recv(1024).decode()
                if not message:
                    break
                print(message)
                # If the message includes a prompt (ends with ":" or contains turn instructions or rematch query),
                # then ask the user for input.
                if ("Your turn" in message) or (message.strip().endswith(":")) or ("Do you" in message):
                    user_input = input("Enter your move/choice: ")
                    self.client_socket.sendall(user_input.encode())
            except Exception as e:
                print("Error:", e)
                break
        self.client_socket.close()

if __name__ == "__main__":
    client = TicTacToeClient()
