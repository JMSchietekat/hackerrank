
import math
import os
import random
import re
import sys


def breakingRecords(scores):
    high = scores[0]
    low = scores[0]

    count_h_l = [0, 0]

    for s in scores:
        if s > high:
            high = s
            count_h_l[0] += 1

        if s < low:
            low = s
            count_h_l[1] += 1

    return count_h_l


if __name__ == '__main__':

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    print(result[0], result[1])
