import socket
import threading
from threading import Thread


class ClientThread(Thread):

    def __init__(self, client_sock, backend_ip):
        Thread.__init__(self)
        self.client_sock = client_sock
        self.backend_ip = backend_ip
        self.backend_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.backend_socket.connect((self.backend_ip, 8001))

    def run(self):
        print("CONECTEI!")

        threading.Thread(target=self.replier, args=(self.backend_socket, self.client_sock))
        data = self.client_sock.recv(4096)
        while True:
            if not data:
                self.client_sock.close()
                self.backend_socket.close()
                break
            self.backend_socket.send(data)
            data = self.client_sock.recv(4096)

    def replier(self):
        data = self.backend_sock.recv(4096)
        while True:
            if not data:
                self.client_sock.close()
                self.backend_socket.close()
                break
            self.client_sock.send(data)
            data = self.backend_socket.recv(4096)
