import math
import os
import random
import re
import sys

def miniMaxSum(arr):
    min = 10e9
    max = 1
    sum = 0

    for e in arr:
        if(e > max):
            max = e
        if(e < min):
            min = e
        sum += e

    return (sum-max), (sum-min)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    res = miniMaxSum(arr)
    print(res[0], res[1])
