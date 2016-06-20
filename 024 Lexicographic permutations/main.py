#!/usr/bin/python3.5

import itertools

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

permutations = itertools.permutations(numbers)

permutations = [int(''.join(map(str, p))) for p in permutations] #convers to list of ints
print(permutations[999999])


