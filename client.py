#!usr/bin/python

import socket
import thread
import time

from Crypto.Hash import SHA512

class Connection:

        def __init__(self, path, ip, port, *args, **kwargs):
                self.path = path
                self.ip = ip
                self.mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.port = port
                if kwargs.get('timeout', None):
                        try:
                                self.timeout = float(kwargs.get('timeout', None))
                        except:
                                print "Cannot set timeout, setting 0.5 as default"
                                self.timeout = 0.5
                else:
                        self.timeout = 0.5
                try:
                        f = open(self.path, 'r')
                        self.file = f.readlines()
                except IOError:
                        print "Cant find path: " + str(self.path)
                        print "Check file and restart the script"
                        exit()
                self.peers = []
                self.sockets = []
                self.databuffer = [] #TODO: named tuple or json
                self.sentAll = 0

        def getpeers(self):
                lines = 0
                for line in self.file:
                        print line
                        lines += 1
                        line = line.split(',')
                        line[0] = str(line[0])
                        line[1] = int(line[1])
                        self.peers.append(line)
                print "Loaded " + str(lines) + " peers."
                return self.peers

        def connect(self):  # TODO: add progressbar from offchuck/textprogressbar
                for a in self.peers:
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        s.settimeout(self.timeout)
                        try:
                                s.connect(tuple(a))
                                self.sockets.append(s)
                        except socket.timeout:
                                print "Cannot connect to: " + str(a[0]) + ':' + str(a[1])
                        s.settimeout(None)
                return self.sockets

        def broadcast(self, message):
                self.connect()
                success = 0
                failed = 0
                for s in self.sockets:
                        try:
                                s.sendall(message)
                                success += 1
                        except socket.timeout:
                                failed += 1
                print "Sent: " + str(success)
                print "Failed: " + str(failed)
                self.sockets = []
                self.sentAll = self.sentAll + success
                return success

        def server(self):
            try:
                self.mysocket.bind((self.ip, self.port))
            except:
                print "Cannot create server..."
                return False
            while 1:
                self.mysocket.listen(1)
                conn, addr = self.mysocket.accept()
                data = conn.recv(1024)
                data = data.split(',')
                self.databuffer.append(data) #TODO: namedtuple or json with hashes
                print str(addr) + " | " + data
            return False

        def sendinfo(self):
            while 1:
                fileHash = SHA512.new()
                fileHash.update('supersafetysalt' + self.file + 'changethisplease')
                fileHash = fileHash.hexdigest()
                data = str(self.ip) + " ," + str(fileHash) + " ," + str(self.file)
                self.broadcast(data)
                time.sleep(1)


test = Connection("test.txt", '127.0.0.1', 5005, timeout=0.5)
test.getpeers()
print test.connect()
thread.start_new_thread(test.sendinfo())
