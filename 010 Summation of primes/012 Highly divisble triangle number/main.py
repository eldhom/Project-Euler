#!/usr/bin/python3.5


import math


def getDivisors(num):
	divisors = 0
	end = int(math.sqrt(num))
	for x in range(1, end+1):
		if(not num%x):
			divisors +=2
	if(end == num**2):
		divisors -=1
	return divisors

def getTriangleNumber(numDivisors):
	count = 1
	divisors =0
	triNum = 0
	while(divisors < numDivisors):
		triNum += count
		divisors = getDivisors(triNum)
		count +=1
	return triNum

print("Trianglenumber with over 500 divisors: " + str(getTriangleNumber(500)))
