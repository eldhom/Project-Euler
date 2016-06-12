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

def sumArray(arr):
	summ = 0
	for x in arr:
		summ += x
	return summ

while(primes[-1] < 2000000):
	print("Prime: " + str(primes[-1]))
	primes.append(getNextCoPrime(primes))
primes.pop()

print("Sum of all primes below 2000000 is: " + str(sumArray(primes)))
