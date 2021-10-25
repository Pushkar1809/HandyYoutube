import socket

class Connect_client():

    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((socket.gethostname(), 3001))
        self.s.listen(5)
        self.client_socket, self.address = self.s.accept()
        print(f"Connection made successfully with {self.address}")


    def send_package(self, obj):
        self.client_socket.send(obj.encode())

    def __del__(self):
        self.client_socket.close()
