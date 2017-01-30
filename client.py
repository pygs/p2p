#!usr/bin/python

class Connection:
        def __init__(self, path):
                self.path = path
                f = open(self.path, 'r')
                self.file =  f.readlines()
                self.peers = []
        def getPeers(self):
                for line in self.file:
                        print line
                        line = line.split(',')
                        line[0] = str(line[0])
                        line[1] = int(line[1])
                        self.peers.append(line)
                return self.peers
                
test = Connection("test.txt")
test.getPeers()
print test.peers
