
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    N = int(input())

    names = []

    for N_itr in range(N):
        firstNameEmailID = input()

        regex = re.search( r'^([a-z]{1,20}) [a-z.]+@gmail.com$', firstNameEmailID)

        if(regex):
            names.append(regex.group(1))

    names.sort()
    
    for name in names:
        print(name)