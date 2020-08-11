import math
import os
import random
import re
import sys


def kaprekarNumbers(p, q):
    numbers = []

    for x in range(p, q+1):
        if(isKaprekarNumber(x)):
            numbers.append(x)

    return numbers


def isKaprekarNumber(n):
    d = len(str(n))
    square = int(math.pow(n, 2))
    p = len(str(square))

    if p > 1:
        if p == d*2:
            l = int(str(square)[:d])
            r = int(str(square)[d:])
        else:
            l = int(str(square)[:d-1])
            r = int(str(square)[d-1:])

    else:
        l = square
        r = 0

    # print(square, l, r)
    return (l + r == n)


if __name__ == '__main__':
    p = int(input())

    q = int(input())

    numbers = kaprekarNumbers(p, q)

    if len(numbers) == 0:
        print('INVALID RANGE')
    else:
        for x in numbers:
            sys.stdout.write(str(x) + ' ')
