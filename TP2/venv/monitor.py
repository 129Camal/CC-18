import time
import socket
import json


from statusTable import statusTable


class Monitor:

    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.table = statusTable()
        self.time = time.time()

    def listening(self):
        while True:
            msg, address = self.socket.recvfrom(1024)
            msg = json.loads(msg.decode())

            if msg["Type"] == 'probe_response':
                end = time.time()
                elapsedtime = end - self.time
                self.table.update(msg, elapsedtime)

    def send(self):
        self.socket.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 20)
        print("Sending message")
        self.time = time.time()

        self.socket.sendto(bytes(json.dumps({"Type": 'probe_request'}), "utf-8"), ("239.8.8.8", 8888))
        print("Message sent")


def main():

    monitor = Monitor()
    monitor.send()
    monitor.listening()


if __name__ == "__main__":
    main()
