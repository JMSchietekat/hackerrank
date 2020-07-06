#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

numSwaps = 0

for i in range(n):

	for j in range(n-1):
		if (a[j] > a[j+1]):
			temp = a[j+1]
			a[j+1] = a[j]
			a[j] = temp

			numSwaps += 1

	if(numSwaps == 0):
		break

print('Array is sorted in {} swaps.'.format(numSwaps))
print('First Element: {}'.format(a[0]))
print('Last Element: {}'.format(a[-1]))