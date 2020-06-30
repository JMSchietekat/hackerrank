import math
import os
import random
import re
import sys

# Task
# Given a base-10 integer, n, convert it to binary (base-2). Then find and print 
# the base-10 integer denoting the maximum number of consecutive 1's
# in n's binary representation.


if __name__ == '__main__':
	n = int(input())
	cnt = 0
	max = 0

	for c in '{0:b}'.format(n):
		if c == '1':
			cnt += 1
			if cnt > max:
				max = cnt
		else:
			cnt = 0
	
	print(max)
