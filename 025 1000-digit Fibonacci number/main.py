#!/usr/bin/python3.5

def getIndex(digits):
	if(digits < 1):
		return -1
	index = 1
	a = 1
	b = 1
	while(len(str(a)) < digits):
		temp   = a+b
		a	   = b
		b	   = temp
		index += 1
	return index

print(getIndex(1000))
	
