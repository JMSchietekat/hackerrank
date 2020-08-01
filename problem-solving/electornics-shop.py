#!/bin/python3

import os
import sys

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    keyboards.sort()
    drives.sort()

    max_price = 0

    if(keyboards[0] + drives[0] > b):
        return -1

    for k in keyboards:
        for d in drives:
            if k + d >= max_price and k + d <= b:
                max_price = k + d

    return max_price    

if __name__ == '__main__':
    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    print(getMoneySpent(keyboards, drives, b))


