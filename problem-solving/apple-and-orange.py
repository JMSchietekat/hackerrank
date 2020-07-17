

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    apples_a = [apple + a for apple in apples]
    oranges_b = [orange + b for orange in oranges]
    
    apples_on_house = [apple for apple in apples_a if s <= apple <= t]
    orranges_on_house = [orange for orange in oranges_b if s <= orange <= t]

    print(len(apples_on_house))
    print(len(orranges_on_house))


if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
