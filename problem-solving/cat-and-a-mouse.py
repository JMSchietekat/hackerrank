import math
import os
import random
import re
import sys

# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    xz = abs(x-z)
    yz = abs(y-z)

    if xz == yz: return 'Mouse C'
    elif xz < yz: return 'Cat A'
    else: return 'Cat B'

if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        print(catAndMouse(x, y, z))

    
