import math
import os
import random
import re
import sys


def birthday(s, d, m):

    count = 0

    for i, _ in enumerate(s):
        total = 0
        for j in range(m):
            if(i+j < len(s)):
                total += s[i+j]

            if(j == (m-1) and total == d):
                count += 1

    return count


if __name__ == '__main__':
    n = int(input().strip())
    s = list(map(int, input().rstrip().split()))
    dm = input().rstrip().split()
    d = int(dm[0])
    m = int(dm[1])

    print(birthday(s, d, m))
