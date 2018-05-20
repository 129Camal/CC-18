import socket
import json
import time
import random
import struct
import psutil


def serverstatus(address):
    cpu = psutil.cpu_percent(interval=None)
    ram = psutil.virtual_memory()

    return {"Type": 'probe_response',
            "RAM": ram[1],
            "CPU": cpu,
            "IP": address[0],
            "Door": address[1]}


class BackEndServer:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind(("", 8888))
        mc_group = socket.inet_aton("239.8.8.8")
        mreq = struct.pack('4sL', mc_group, socket.INADDR_ANY)
        self.socket.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

        self.listening()


    def listening(self):
        while True:
            print("Waiting for message")
            message, address = self.socket.recvfrom(1024)
            msg = json.loads(message.decode())

            if msg['Type'] == 'probe_request':
                message = json.dumps(serverstatus(address)).encode()

                n = random.randint(0, 10)
                time.sleep(n * 0.001)
                self.socket.sendto(message, address)




def main():
    BackEndServer()


if __name__ == "__main__":
    main()
