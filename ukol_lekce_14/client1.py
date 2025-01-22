import socket
import threading

class TicTacToeClient1:
    def __init__(self, host='127.0.0.1', port=65450):
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

                # Určení hráče
                if "You are player" in message:
                    self.player = message.split()[-1]
                    print(f"Assigned as player {self.player}")

                # Konec hry
                elif "wins" in message or "draw" in message or "loses" in message:
                    print("Konec hry!")
                    break

            except Exception as e:
                print(f"Error receiving message: {e}")
                break

    def send_message(self, message):
        try:
            self.client_socket.send(message.encode())
            print(f"Sent message: {message}")
        except Exception as e:
            print(f"Error sending message: {e}")

    def run(self):
        while self.player is None:
            pass  # Čekání na přiřazení hráče

        while True:
            try:
                message = input("Zadej svůj tah (0-8) nebo napiš 'stop' pro ukončení hry: ")
                self.send_message(message)
                if message.lower() == 'stop':
                    break
            except Exception as e:
                print(f"Error during input: {e}")
                break

        self.client_socket.close()
        print("Disconnected from server.")

if __name__ == '__main__':
    client = TicTacToeClient1()
    client.run()
