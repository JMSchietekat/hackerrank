import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    b_charged = 0
    b_actual = 0

    for e in bill:
        b_charged += e

    b_actual = (b_charged - bill[k]) / 2
    
    return 'Bon Appetit' if b == b_actual else int(b - b_actual)



if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    print(bonAppetit(bill, k, b))
