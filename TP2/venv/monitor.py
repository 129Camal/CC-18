import socket
import json

def proberequest():
    return {}

class Monitor:

    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind(('', 8888))
        self.listening();
        self.sendrequest();

    def listening(self):
        while True:
            msg, address = self.socket.recvfrom(1024)
            msg = json.loads(msg.decode())

            print(msg, address)

    def sendrequest(self):
        self.socket.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 20)

        self.socket.sendto({"Type": 'probe_request'}, ("239.8.8.8", 8888))
