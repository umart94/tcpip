import string
import random
import sys

#Generate key, allowing characters, digits, special characters. 
key = ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits + '^!\$%&/()=?{[]}+~#-_.:,;<>|\\') for _ in range(2000))
print(key)

#print key in executing window
print('\n'+'Key length = '+str(len(key)))

#print key into file in current folder
with open('key.txt', 'w') as w:
	w.write(key)
	w.close()
