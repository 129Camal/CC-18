import time
import socket
import json
from threading import Thread


class Monitor:

    def __init__(self, statusTable):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.table = statusTable
        self.time = time.time()

        t1 = Thread(target=self.listening)
        t1.start()

        t2 = Thread(target=self.send)
        t2.start()

    def listening(self):
        while True:
            msg, address = self.socket.recvfrom(1024)
            msg = json.loads(msg.decode())

            if msg["Type"] == 'probe_response':
                end = time.time()
                elapsedtime = end - self.time
                self.table.update(msg, elapsedtime)
                self.table.printdict()

    def send(self):
        while True:

            print("Sending message")
            self.time = time.time()

            self.socket.sendto(bytes(json.dumps({"Type": 'probe_request'}), "utf-8"), ("239.8.8.8", 8888))
            print("Message sent")

            time.sleep(5)


def main():
    Monitor()


if __name__ == "__main__":
    main()
