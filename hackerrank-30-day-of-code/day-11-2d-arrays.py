import math
import os
import random
import re
import sys

def calculateHourglassTotal(arr, start = (0,0)):
    total = 0
    
    for i in range(0,3):
		# Sum top row
        total += arr[start[0]][start[1]+i]
		# Sum bottom row
        total += arr[start[0]+2][start[1]+i]

	# Add centre
    total += arr[start[0]+1][start[1]+1]

    return total


if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    # -9 <= A[i][j] <= 9 thus smallest starting value should be
	max = -9*7

    for i in range(4):
        for j in range(4):
            temp = calculateHourglassTotal(arr, (i,j))
            if(temp > max):
                max = temp

    print(max)

