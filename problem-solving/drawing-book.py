#!/bin/python3

import os
import sys
import math


def pageCount(n, p):
    pageTurns = math.floor(p/2)
    totalTurns = math.floor(n/2)

    return min(pageTurns, totalTurns - pageTurns)


if __name__ == '__main__':

    n = int(input())

    p = int(input())

    print(pageCount(n, p))
