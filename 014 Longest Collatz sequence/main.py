#!/usr/bin/python3.5

lengths = {}

def collatzLength(num):
	length = 1
	while(num > 1):
		if(num in lengths):
			return lengths[num]+length
		elif(not num%2):
			num /=2
		else:
			num = num*3+1
		length += 1
	return length


longest = 0
num = 0
for x in range(0, 1000000):
	length = collatzLength(x)
	lengths[x] = length
	if(longest < length):
		longest = length
		num = x
		

print(str(num))


