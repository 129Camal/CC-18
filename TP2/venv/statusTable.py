class statusTable:
    def __init__(self):
        self.dictionary = {}

    def update(self, msg, elapsedtime):

        for key in self.dictionary:
            if self.dictionary[key]['IP'] == msg['IP']:
                del self.dictionary[key]

                break

        diction = {'RAM': msg['RAM'],
                   'CPU': msg['CPU'],
                   'IP': msg['IP'],
                   'Door': msg['Door'],
                   'RTT': elapsedtime}

        ram = msg['RAM']
        cpu = msg['CPU']

        formula = (ram * (1 - (cpu * 0.01)) * elapsedtime) / 3

        self.dictionary[formula] = diction

        self.dictionary = SortedDisplayDict(self.dictionary)

    def printdict(self):
        print(self.dictionary)


    def bestServer(self):

        posicao = max(self.dictionary, key=float)
        ip = self.dictionary[posicao]['IP']
        return ip


class SortedDisplayDict(dict):
    def __str__(self):
        return "{" + ", ".join("%r: %r" % (key, self[key]) for key in sorted(self)) + "}"
