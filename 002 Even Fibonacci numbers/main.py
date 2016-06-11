#!/usr/bin/python3.5

#old solution
"""def sumEvenFibonacci(first, second):
	if(second > 4000000):
		return 0
	x = 0
	if(not second%2):
		x = second
	return x + sumEvenFibonacci(second, first+second)
print(sumEvenFibonacci(1,2))"""

summ =0
x = 1
y = 2
while(y < 4000000):
	summ += y
	for i in range(0,3):
		temp = y
		y = x+y
		x = temp

print(summ)

