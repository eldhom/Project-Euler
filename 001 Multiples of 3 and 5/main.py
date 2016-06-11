#!/usr/bin/python3.5
import sys
import math

upperBoundary = 1000
lowerBoundary = 0

def sumMultiples(multiple, upperBoundary, lowerBoundary):
	summ = 0
	for x in range(lowerBoundary, upperBoundary):
		if(not x%multiple):
			summ += x
	return summ


sys.argv.pop(0)
try:
	i = sys.argv.index('-u')
	sys.argv.pop(i)
	upperBoundary = int(sys.argv.pop(i))
except:
	print("Using default upper boundary")
	
try:
	i = sys.argv.index('-l')
	sys.argv.pop(i)
	lowerBoundary = int(sys.argv.pop(i))
	if(lowerBoundary < 0):
		raise Exception
except:
	print("Using default lower boundary")

if(not len(sys.argv) is 2):
	print("Error: Wrong number of arguments")

try:
	first 	= int(sys.argv[0])
	second	= int(sys.argv[1])
	try:
		print(sumMultiples(first, upperBoundary, lowerBoundary) + sumMultiples(second, upperBoundary, lowerBoundary) - sumMultiples(first*second, upperBoundary, lowerBoundary))
	except ZeroDivisionError:
		print(math.nan)
except:
	print("Error: Invalid input - '" + num + "' is - " + str(type(num)))




