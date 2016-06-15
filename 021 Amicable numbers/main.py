#!/usr/bin/python3.5

import math

def getDivisors(num):
	divisors = list()
	for x in range(1, int(num/2+1)):
		if(num%x == 0):
			divisors.append(x)
	return divisors

def getAmicableNumbersInRange(start, stop):
	amicableNumbers = list()
	for x in range(start, stop):
		divisors = getDivisors(x)
		num = sum(divisors)
		if(sum(getDivisors(num)) == x and num != x):
			print(str(x) + ": " + str(divisors))
			amicableNumbers.append(x)
	print("Amicable numbers: " + str(amicableNumbers))
	return amicableNumbers


print("The sum is: " + str(sum(getAmicableNumbersInRange(1, 10000))))

