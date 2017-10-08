#!/usr/bin/env python
#client side outbound outline

import socket

TCP_IP = '127.0.0.1'                                        # server ip
TCP_PORT = 5005
BUFFER_SIZE = 1024
MESSAGE = "Queue ready!"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE)
data = s.recv(BUFFER_SIZE)
s.close()

print "received data:", data
