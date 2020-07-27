import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    ar.sort()
    pairs = 0
    prev = 0

    for e in ar:
        if e == prev:
            pairs += 1
            prev = 0
        else:
            prev = e

    return pairs



if __name__ == '__main__':

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    print(int(sockMerchant(n, ar)))