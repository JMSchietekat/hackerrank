
import math
import os
import random
import re
import sys


def getTotalX(a, b):
    x = a[len(a)-1]
    y = b[0]
    count = 0

    for p in range(x, y+1):
        f1 = False
        for i in b:
            if i % p != 0:
                f1 = True
                break
        f2 = False
        for i in a:
            if p % i != 0:
                f2 = True
                break
        if not f1 and not f2:
            count += 1
    return count


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    print(getTotalX(arr, brr))
