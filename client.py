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
                        s.connect(tuple(a))
                        self.sockets[i] = s
                        i += 1
                return self.sockets
        
test = Connection("test.txt")
print test.getPeers()
test.connect()
