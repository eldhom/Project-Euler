#!/usr/bin/python3.5

import math

def getNumPaths(n):
	return math.factorial(2*n)/math.pow(math.factorial(n),2)
	

print(str(getNumPaths(20)))





