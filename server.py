#!/usr/bin/env python
#server side outline

import socket

TCP_IP = '127.0.0.1'                                        # client ip
TCP_PORT = 5005
BUFFER_SIZE = 20  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
print 'Connection address:', addr
while 1:
    data = conn.recv(BUFFER_SIZE)                       # in this case, 'data' will be
                                                        # that you should accept queue
    if not data: break
    print "received queue notification:", data
    response = input('What is your response?')
    if response is 'yes':
        conn.send(data)  # echo
conn.close()
