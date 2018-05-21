import socket
from threading import Thread
import socketserver


class Client(Thread):

    def __init__(self, client_sock, backend_ip):
        Thread.__init__(self, backend_ip)
        self.client_sock = client_sock
        self.backend_ip = backend_ip

    def run(self, backend_ip):
        backend_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        backend_socket.connect((backend_ip, 80))

        data = self.client_sock.recv(4086)
        while True:
            if not data:
                self.backend_socket.close()
                break
            self.backend_socket.send(data)
