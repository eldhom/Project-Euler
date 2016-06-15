#!/usr/bin/python3.5

def getAlphabeticalScore(text):
	text = text.upper()
	score = 0
	for c in text :
		score += ord(c) - 64
	return score

names = open("names.txt")
names = [c.replace("\"", "") for c in names.read().split(",")]
names.sort()


multiplier = 1
total =0 
for name in names:
	total += getAlphabeticalScore(name)*multiplier
	multiplier += 1

print(total)

	
