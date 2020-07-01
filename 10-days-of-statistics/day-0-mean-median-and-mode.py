
def mean(elem=[]):
    mean = 0

    for i in elem:
        mean += i

    return round(mean / len(elem), 1)


def median(elem=[]):
    elem.sort()
    median = 0
    elem_cnt = len(elem)

    if(elem_cnt % 2 == 0):
        median = (elem[int(elem_cnt/2) - 1] + elem[int(elem_cnt/2)])/2
    else:
        median = elem[int(elem_cnt/2)]

    return round(median, 1)


def mode(elem=[]):
    elem.sort()
    mode = 0
    local_occurance = 0
    max_occurance = 0

    for i, e in enumerate(elem):
        if (i == 0):
            mode = e
            local_occurance = 1
            continue

        if(e == elem[i-1]):
            local_occurance += 1
            if(local_occurance > max_occurance):
                max_occurance = local_occurance
                mode = e
            continue

        local_occurance = 1

    return round(mode, 1)

if __name__ == "__main__":

    n = int(input())

    elem = list(map(int, input().rstrip().split()))

    print(mean(elem))
    print(median(elem))
    print(mode(elem))
