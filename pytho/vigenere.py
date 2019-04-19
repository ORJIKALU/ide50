import sys
from cs50 import get_string

# if the commandline argument is not given or more than 2 return 1
if(len(sys.argv)  != 2):
	print("incorrect input")
	exit(1)
m = len(sys.argv[1])
key = sys.argv[1]
for i in range(m):
	if(not (sys.argv[1][i]).isalpha()):
		print("usage")
		exit(1)
user = get_string()
n = len(user)
j = 0

for i in range(n):
	if(user[i].isalpha):
		if(key[j].islower()):
			hashkey = ord(key[j]) - ord('a')
			print({hashkey})
		else:
			hashkey = ord(key[j]) - ord('A')
		if(user[i].isupper):
			hash = (ord(user[i]) + hashkey)
			if(hash > ord('Z')):
				hash = hash - ord("A") + hashkey
				print({chr(hash)}, end='')
		if(user[i].islower):
			hash = (ord(user[i])+ hashkey)
			if(hash> ord('z')):
				hash = hash - ord('a') + hashkey
				print({chr-})
				


			

print()