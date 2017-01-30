
#!usr/bin/python

import socket

class Connection:
        def __init__(self, path):
                self.path = path
                f = open(self.path, 'r')
                self.file =  f.readlines()
                self.peers = []
                self.sockets = []
        def getPeers(self):
                for line in self.file:
                        print line
                        line = line.split(',')
                        line[0] = str(line[0])
                        line[1] = int(line[1])
                        self.peers.append(line)
                return self.peers
        def connect(self):
                i = 0
                for a in self.peers:
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        s.settimeout(0.5)
                        try:
                                s.connect(tuple(a))
                        except:
                                print "Cannot connect to: " + str(a[0])
                        self.sockets.append(s)
                        i += 1
                return self.sockets
test = Connection("test.txt")
test.getPeers()
print test.connect()

