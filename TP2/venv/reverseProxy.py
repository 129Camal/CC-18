from monitor import Monitor
from Client import Client
import socket
from statusTable import statusTable


def main():
    s = statusTable()
    m = Monitor(s)
    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    tcp_server.bind(('localhost', 8001))
    threads = []

    while True:
        tcp_server.listen(30)
        print("CHEGUEI")
        client_socket = tcp_server.accept()
        print("CHEGUEI2")
        bestserver = s.bestServer()
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.connect((bestserver, 8000))
        thread = Client.Client(client_socket, server)
        thread.start()
        threads.append(thread)


if __name__ == "__main__":
    main()
