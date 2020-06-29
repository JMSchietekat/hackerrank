#!/bin/python3

import os
import sys


def consecutiveSum(n, scan=(0, 1)):
    scan = (scan[0], scan[1]+1)

    assert scan[1] >= scan[0], 'scan range must at least include 1 digit'
    assert scan[0] >= 0, 'scan indices must be positive'
    assert scan[1] >= 0, 'scan indices must be positive'

    total = 0
    num = str(n)

    for x in range(scan[0], scan[1]):
        total += int(num[x])

    return total


def isPrime(n):
    if (n < 2):
        return False
    if (n == 2):
        return True
    if (n % 2 == 0):
        return False

    for m in range(3, int(n/2)+1, 2):
        if (n % m == 0):
            return False

    return True


def primeDigitSums(n):
    if (len(str(n)) >= 6):
        if(not isPrime(consecutiveSum(n, (2, 5)))):
            return False
        if(not isPrime(consecutiveSum(n, (3, 5)))):
            return False
        if(not isPrime(consecutiveSum(n, (1, 5)))):
            return False

    if (len(str(n)) >= 5):
        if(not isPrime(consecutiveSum(n, (2, 4)))):
            return False
        if(not isPrime(consecutiveSum(n, (1, 4)))):
            return False
        if(not isPrime(consecutiveSum(n, (0, 4)))):
            return False

    if (len(str(n)) >= 4):
        if(not isPrime(consecutiveSum(n, (1, 3)))):
            return False
        if(not isPrime(consecutiveSum(n, (0, 3)))):
            return False
        if(not isPrime(consecutiveSum(n, (0, 2)))):
            return False

    return True


if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        n = int(input())

        cnt = 0

        for x in range(10**(n-1), 10**(n)-1):
            if(primeDigitSums(x)):
                cnt += 1

        print(cnt % (10**9 + 7))
