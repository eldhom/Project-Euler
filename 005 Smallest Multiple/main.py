#!/usr/bin/python3.5

import math

def isPrime(num):
	for x in range(2, num):
		if(not num%x):
			return False
	return True
	
def getNextPrime(num):
	prime = num+1
	while(not isPrime(prime)):
		prime +=1
	return prime
	

def addList(l, i, v):
	try:
		l[i] +=v
	except IndexError:
		for x in range(0, i-len(l)+1):
			l.append(0)
		l[i] = v
	return l

		

def getPrimeFactors(num):
	
	primes = list()
	prime = 2
	while(not num is 1):
		if(not num%prime):
			num = int(num/prime)
			primes = addList(primes, prime, 1)
		else:
			prime = getNextPrime(prime)
	return primes

def getSmallestMultiple(num):
	primes = list()
	smallestMultiple = 1
	for x in range(2, num+1):
		arr = getPrimeFactors(x)
		for y in range(0, len(arr)):
			if(len(primes) > y):
				if(primes[y] < arr[y]):
					primes[y] = arr[y]
			else:
				primes.append(arr[y])
	for x in range(0, len(primes)):
		smallestMultiple = smallestMultiple * math.pow(x,primes[x])
	return smallestMultiple

print("Smallest multiple is: " + str(getSmallestMultiple(20)))
