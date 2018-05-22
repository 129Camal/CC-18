import socket
from threading import Thread


class ClientThread(Thread):

    def __init__(self, client_sock, backend_ip):
        Thread.__init__(self)
        self.client_sock = client_sock
        self.backend_ip = backend_ip

    def run(self):
        backend_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        backend_socket.connect((self.backend_ip, 8002))
        print("CONECTEI!")

        data = self.client_sock.recv(4086)
        while True:
            if not data:
                backend_socket.close()
                break
            backend_socket.send(data)
