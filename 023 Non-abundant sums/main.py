#!/usr/bin/python3.5

LIMIT = 28124
divsum = [0]*LIMIT
for i in range(1, LIMIT):
	for j in range(i*2, LIMIT, i):
		divsum[j] += i
abundantNumbers = [i for (i, x) in enumerate(divsum) if x > i]

expressible = [False]*LIMIT
for i in abundantNumbers:
	for j in abundantNumbers:
		if (i+j < LIMIT):
			expressible[i+j] = True
		else:
			break

total = sum(i for(i, x) in enumerate(expressible) if not x)
print(total)
