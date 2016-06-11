#!/usr/bin/python3.5

def isPalindrome(s):
	if(len(s) == 0):
		return True
	elif(len(s) is 1):
		return False
	elif(s[0] is s[-1]):
		return isPalindrome(s[1:-1])

def largestPalindromeProduct(minimum, maximum):
	summ =0
	for x in range(minimum, maximum):
		for y in range(x, maximum):
			z = x*y
			if(isPalindrome(str(z))):
				if(z > summ):
					summ = z
	return summ

print(largestPalindromeProduct(100, 1000))
			
		
