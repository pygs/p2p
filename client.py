#!usr/bin/python

import socket


class Connection:

        def __init__(self, path, *args, **kwargs):
                self.path = path
                if kwargs.get('timeout', None):
                        self.timeout = float(kwargs.get('timeout', None))
                else:
                        self.timeout = 0.5
                f = open(self.path, 'r')
                self.file = f.readlines()
                self.peers = []
                self.sockets = []

        def getpeers(self):
                for line in self.file:
                        print line
                        line = line.split(',')
                        line[0] = str(line[0])
                        line[1] = int(line[1])
                        self.peers.append(line)
                return self.peers

        def connect(self):  # TODO: add progressbar from offchuck/textprogressbar
                for a in self.peers:
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        s.settimeout(self.timeout)
                        try:
                                s.connect(tuple(a))
                                self.sockets.append(s)
                        except:
                                print "Cannot connect to: " + str(a[0]) + ':' + str(a[1])
                return self.sockets

        def broadcast(self, message):
                ok = 0
                failed = 0
                for s in self.sockets:
                        try:
                                s.send(message)
                                ok += 1
                        except socket.timeout:
                                failed += 1
                print "Sended: " + str(ok)
                print "Failed: " + str(failed)


test = Connection("test.txt", 0.5)
test.getpeers()
print test.connect()
test.broadcast("xD")


