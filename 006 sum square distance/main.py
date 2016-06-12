#!/usr/bin/python3.5

import math

def squareOfSums(num):
	return math.pow(((num*(num+1))/2),2)

def sumOfSquares(num):
	return num*(num+1)*(2*num +1)/6


x = squareOfSums(100)
y = sumOfSquares(100)
print("Difference between square of sums: " + str(x) + " and sum of squares: " + str(y) + " is: " + str(x-y))
