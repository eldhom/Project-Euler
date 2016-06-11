#!/usr/bin/python3.5
import math

primes 		= [2]

def isRelativelyPrime(num, primes):
	for x in primes:
		if(x > math.sqrt(num)):
			return True
		if(not num%x):
			return False
	return True

def getNextCoPrime(primes):
	prime = primes[-1]+1
	while(not isRelativelyPrime(prime, primes)):
		prime += 1
	return prime

for i in range(1, 10001):
	primes.append(getNextCoPrime(primes))

print("10001st prime is: " + str(primes[-1]))
