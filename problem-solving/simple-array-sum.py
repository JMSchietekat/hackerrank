
import os
import sys

def simpleArraySum(ar):
    sum = 0

    for e in ar:
        sum += e

    return sum

if __name__ == '__main__':

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    print(simpleArraySum(ar))

