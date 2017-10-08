#!/usr/bin/env python
#client side outbound outline

import socket

# change to server ip
TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024
MESSAGE = "Queue ready!"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE)
data = s.recv(BUFFER_SIZE)
s.close()

# script will send the same data that it will receive
# once the dataq is received, it will be taken as confirmation
print "received data:", data
