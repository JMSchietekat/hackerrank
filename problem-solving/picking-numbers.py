import math
import os
import random
import re
import sys

def pickingNumbers(a):
    a.sort()
    max = 0

    for i, e in enumerate(a):
        if(i == len(a)):
            continue

        local_max = 1

        for j in range(i, len(a)-1):
            if a[j+1] - a[i] <= 1:
                local_max += 1
                if local_max > max:
                    max = local_max
            else: 
                break

    return max

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    print(pickingNumbers(a))
