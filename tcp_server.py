#! /usr/bin/python3

import socket

# TCP/IP address, port to listen on, and /
# buffer size of the data to capture.

TCP_IP = "192.168.181.190"
TCP_PORT = input("Enter the TCP port you would like to scan: ")
BUFFER_SIZE = 100

# Defines the socket, binds the socket to the IP /
# address and port using the variables. Then tells /
# the socket to listen using the listen() method. 

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

# Captures the IP address and port of the connecting /
# system using accept(), then print.

conn,addr = s.accept()
print ('Connection address: ', addr)

# Python continues to check for data until stopped. /
# The information gets placed into a buffer and printed.

while 1:

	data = conn.recv(BUFFER_SIZE)
	if not data:break
	print("Received data: ", data)
	conn.send(data) #echo
conn.close