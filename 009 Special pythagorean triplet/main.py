#!/usr/bin/python3.5

import math

for c in range(0, 1000):
	for b in range(0, c):
		for a in range(0, b):
			if(a + b +c == 1000):
				if(math.pow(a, 2) + math.pow(b, 2) == math.pow(c, 2)):
					print("a+b+c: " + str(a) + "+" + str(b)  + "+" + str(c) + "=" + str(a+b+c))
					print("a² + b² = c²: " + str(math.pow(a, 2)) + "+" + str(math.pow(b, 2)) + "=" + str(math.pow(c, 2)))
					print("a*b*c:" + str(a) + "*" + str(b) + "*" + str(c) + "=" + str(a*b*c))
					exit()
