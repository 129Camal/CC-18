from monitor import Monitor
import Client
import socket
from statusTable import statusTable


def main():
    s = statusTable()
    m = Monitor(s)
    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    tcp_server.bind(('localhost', 8000))
    threads = []

    while True:
        tcp_server.listen(30)
        print("CHEGUEI")
        client_socket = tcp_server.accept()
        print("Recebi uma comunicação")
        bestserver = s.bestServer()
        print("Connectar ao server")
        print(bestserver)
        thread = Client.ClientThread(client_socket, bestserver)
        thread.start()
        print("Thread Cliente-Server ativa!")
        threads.append(thread)
        print("Anexei a Thread!")


if __name__ == "__main__":
    main()
