#!/usr/bin/python3.5


def getDigitSum(num):
	summ =0
	for c in str(num):
		summ += int(c)
	return summ

print("Digit sum of 2¹⁰⁰⁰ is: " + str(getDigitSum(2**1000)))
		
