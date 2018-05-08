import socket
import json


def serverstatus():
    return {"Type": 'probe_response',
            "RAM": 3000,
            "CPU": 20345}


class BackEndServer:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind(('monitor', 8888))
        self.listening()
        self.presence()

    def listening(self):
        while True:
            message, address = self.socket.recvfrom(1024)
            msg = json.loads(message.decode())
            print(msg, address)

            if msg['Type'] == 'probe_request':
                message = json.dumps(serverstatus()).encode()
                self.sock.sendto(message, address)

    def presence(self):
        inf = {"Type": 'registration'}
        message = json.dumps(inf).encode("UTF-8")
        self.sock.sendto(message, ('monitor', 8888))


def main():
    BackEndServer()
