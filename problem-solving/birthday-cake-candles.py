import math
import os
import random
import re
import sys

def birthdayCakeCandles(ar):

    max = 0
    max_cnt = -1

    for e in ar:
        if(e > max):
            max = e
            max_cnt = 0
        if(e == max):
            max_cnt += 1

    return max_cnt


if __name__ == '__main__':
    ar_count = int(input())
    
    arr = list(map(int, input().rstrip().split()))

    print(birthdayCakeCandles(arr))
