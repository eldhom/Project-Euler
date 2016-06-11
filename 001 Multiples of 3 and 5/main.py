#!/usr/bin/python3.5
import sys
import math

def multiples(multiple, maxTest):
	count = 0
	for x in range(0, maxTest):
		if(not x%multiple):
			count += 1

	return count


sys.argv.pop(0)
for num in sys.argv:
	try:
		num = int(num)
		try:
			print(multiples(num, 1000) + multiples(num, 1000) - multiples(num, 1000))
		except ZeroDivisionError:
			print(math.nan)
	except:
		print("Error: Invalid input - '" + num + "' is - " + str(type(num)))




