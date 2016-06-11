#!/usr/bin/python3.5
import sys
import math

upperBoundary = 1000
lowerBoundary = 0

def multiples(multiple, upperBoundary, lowerBoundary):
	count = 0
	for x in range(lowerBoundary, upperBoundary):
		if(not x%multiple):
			count += 1

	return count


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

if(not len(sys.argv)):
	print("Error: Wrong number of arguments")

for num in sys.argv:
	try:
		num = int(num)
		try:
			print(multiples(num, upperBoundary, lowerBoundary) + multiples(num, upperBoundary, lowerBoundary) - multiples(num, upperBoundary, lowerBoundary))
		except ZeroDivisionError:
			print(math.nan)
	except:
		print("Error: Invalid input - '" + num + "' is - " + str(type(num)))




