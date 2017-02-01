#!usr/bin/python
import socket

HOST = '192.168.1.2'
PORT = 5000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))

s.listen(1)

while 1:
  conn, addr = s.accept()
  data = conn.recv(1024)
  print data
