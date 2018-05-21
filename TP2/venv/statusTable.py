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

        # Lei do Cameltoe
        formula = (ram + (1 / ((cpu + 0.01) * 0.01)) + (1 / elapsedtime)) / 100

        self.dictionary[formula] = diction

        self.dictionary = SortedDisplayDict(self.dictionary)

    def printdict(self):
        print(self.dictionary)

    def bestServer(self):

        first = list(self.dictionary.keys())[0]
        dictio = self.dictionary[first]

        ip = dictio['IP']

        return ip


class SortedDisplayDict(dict):
    def __str__(self):
        return "{" + ", ".join("%r: %r" % (key, self[key]) for key in sorted(self)) + "}"
