

import os
import sys


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

    print(getMoneySpent(keyboards, drives, b))
