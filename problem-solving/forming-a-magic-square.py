
import math
import os
import random
import re
import sys

def formingMagicSquare(s):
	return isMagicSquare(s)

def isMagicSquare(s):
	magicNumber = 0
	positiveDiagonalMagicNumber = 0
	negativeDiagonalMagicNumber = 0


	for i, row in enumerate(s):
		localMagicNumber = 0
		for j, e in enumerate(row):
			if(i == 0):
				magicNumber += e
			else:
				localMagicNumber += e

		if(i == j):
			positiveDiagonalMagicNumber += row[j]
			print(row[j])
		
		if(i == -j):
			negativeDiagonalMagicNumber += row[j]
			# print(row[j])
		
		if(i > 0 
			and not magicNumber == localMagicNumber
			and not magicNumber == positiveDiagonalMagicNumber
			and not magicNumber == negativeDiagonalMagicNumber):
			return False

	return True

if __name__ == '__main__':
    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    print(formingMagicSquare(s))


