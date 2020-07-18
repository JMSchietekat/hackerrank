
import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
	if(x1 > x2 and v1 >= v2):
		return "NO"

	if(x2 > x1 and v2 >= v1):
		return "NO"

	k1 = x1
	k2 = x2
	
	for _ in range(int(10e3)):
		k1 += v1
		k2 += v2

		if(k2 == k1):
			return "YES"

		if(x1 > x2 and k2 > k1):
			return "NO"
		if(x2 > x1 and k1 > k2):
			return "NO"	


if __name__ == '__main__':

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    print(kangaroo(x1, v1, x2, v2))

    
