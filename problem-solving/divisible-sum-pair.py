
import math
import os
import random
import re
import sys


def divisibleSumPairs(n, k, ar):
    cnt = 0

    for i in range(n):
        for j in range(i+1, n):
            temp = ar[i] + ar[j]
            # print('A={}, B={}, A+B={}'.format(ar[i], ar[j], temp))
            if(temp % k == 0):
                cnt += 1

    return cnt


if __name__ == '__main__':

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    print(divisibleSumPairs(n, k, ar))
