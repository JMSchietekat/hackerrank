

import math
import os
import random
import re
import sys


def staircase(n):
    line = '#'

    for _ in range(n):
        print(line.rjust(n))
        line += '#'


if __name__ == '__main__':
    n = int(input())

    staircase(n)
