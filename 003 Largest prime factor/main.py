#!/usr/bin/python3.5

number = 600851475143

def isDivisibleBy(num, numbers):
	for x in numbers:
		if(not num%x):
			return True
	return False

def largestPrimeFactor(num):
	primes = list()
	for x in range(2,num):
		if(x > num):
			break
		if(not isDivisibleBy(x, primes)):
			if(not num%x):
				num = num/x
				print("New Factor: " + str(x))
				primes.append(x)
	return primes.pop()


print("Largest Factor is: " + str(largestPrimeFactor(number)))
