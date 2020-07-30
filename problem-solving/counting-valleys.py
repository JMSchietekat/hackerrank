import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    valleys = 0
    alt = 0
    alt_prev = 0

    for i, e in enumerate(s):
        if i > 0:
            alt_prev = alt

        if e == 'D':
            alt -= 1
        elif e == 'U':
            alt += 1

        if alt_prev == 0 and alt == -1:
            valleys += 1

    return valleys


if __name__ == '__main__':

    n = int(input())

    s = input()

    print(countingValleys(n, s))