
import math
import os
import random
import re
import sys


def migratoryBirds(arr):
    arr.sort(reverse=True)
    # print(arr)
    mostcommonId = 0
    max_cnt = 0
    local_cnt = 0

    for i, e in enumerate(arr):
        if i == 0:
            mostcommonId = e
            continue

        elif arr[i-1] == e:
            local_cnt += 1
            if local_cnt == max_cnt:
                mostcommonId = e
            elif local_cnt > max_cnt:
                max_cnt += 1
                mostcommonId = e

        else:
            local_cnt = 0

    return mostcommonId


if __name__ == '__main__':

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    print(migratoryBirds(arr))
