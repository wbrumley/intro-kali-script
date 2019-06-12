#! /usr/bin/python3

import socket

Ports = [21,22,25,3306]

ipAddress = input("Enter the IP address you would like to scan: ")

for i in range (0,4):


		s = socket.socket()

		Port = Ports[i]

		print ('This is the Banner for the Port')

		print(Port)
		
		try:

			s.connect((ipAddress ,Port[i])) 

			answer = s.recv(1024)

			print (answer)

		except:

			print ("no answer")

s.close()