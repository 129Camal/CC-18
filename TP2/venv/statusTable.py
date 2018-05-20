
class statusTable:
    def __init__(self):
        self.dictionary = {}

    def update(self, msg, elapsetime):

        diction = {'RAM': msg['RAM'], 'CPU': msg['CPU'], 'IP': msg['IP'], 'Door': msg['Door'], 'RTT': elapsetime}

        self.dictionary[1] = diction
        print(self.dictionary[1])
