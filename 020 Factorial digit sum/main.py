#!/usr/bin/python3.5

import math

num = math.factorial(100)
numbers = [int(c) for c in str(num)]
	
print(str(sum(numbers)))
