#This program is created by Alexey Titov and Shir Bentabou
#Try To modify it by your own

#libraries
import os
import string
import random
import sys

file = open(input("enter your key file location: "),"rb")  
key = file.read()
file.close()

#decryption function (same as encryption function)
def str_xor(s1, s2):
        return "".join([chr(ord(c1) ^ ord(c2)) for (c1,c2) in zip(s1,s2)])


def filelist():
        mylist = []
        for root, dirs, files in os.walk("c:\\Games"):
                for file in files:
                    if file.endswith(".encrypted"):
                        mylist.append(os.path.join(root, file))

        return mylist

print(filelist())
local = filelist()


def file_decrypt(key, files):    
        for name in files:
                if (name!="DEC.py"): 
                    with open(name,'rb') as f:
                        data = f.read()
                        f.close()
                                
                        #decrypt using function
                        decrypted = str_xor(data, key.strip('\n'))
                        decrypted_file = name + ".decrypted"
                        try:
                                with open(decrypted_file, 'wb') as f:
                                        f.write(decrypted)
                                        f.close()
                                os.remove(name)
                        except:
                                continue

file_decrypt(key, local)
