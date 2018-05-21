from monitor import Monitor
from statusTable import statusTable
from Client import Client

import socket
import thread
from statusTable import statusTable


def main():
    s = statusTable()
    Monitor(s)
    tcpserver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcpserver.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    tcpserver.bind(('localhost', 80))
    threads = []

    while True:
        tcpserver.listen(30)
        (client_socket, (ip, port)) = tcpserver.accept()
        backend_ip = statusTable.bestServer()
        thread = Client.Client(client_socket, backend_ip)
        thread.start()
        threads.append(thread)


if __name__ == "__main__":
    main()
