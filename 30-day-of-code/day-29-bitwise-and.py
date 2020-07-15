
import math
import os
import random
import re
import sys


def process(n, k):
    max = 0

    for i in range(1, n+1):
        for j in range(i+1, n+1):
            temp = i & j
            # print('A={}, B={}, A&B={}'.format(i, j, temp))
            if(temp >= k):continue
            if(temp <= max):continue
            if(temp == k-1):return temp
            
            max = temp
            
    return max


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n, k = map(int, input().split())

        # print(process(n, k))
        print(k-1 if ((k-1) | k) <= n else k-2)
