
def mean(x=[]):
    mean = 0

    for i in x:
        mean += i

    return mean / len(x)


def median(x=[]):
    x.sort()
    x_cnt = len(x)

    if(x_cnt % 2 == 0):
        return (x[int(x_cnt/2) - 1] + x[int(x_cnt/2)])/2
    else:
        return x[int(x_cnt/2)]


def mode(x=[]):
    x.sort()
    mode = 0
    local_occurance = 0
    max_occurance = 0

    for i, e in enumerate(x):
        if (i == 0):
            mode = e
            local_occurance = 1
            continue

        if(e == x[i-1]):
            local_occurance += 1
            if(local_occurance > max_occurance):
                max_occurance = local_occurance
                mode = e
            continue

        local_occurance = 1

    return mode


if __name__ == "__main__":

    n = int(input())

    x = list(map(int, input().rstrip().split()))

    print(round(mean(x), 1))
    print(round(median(x), 1))
    print(round(mode(x), 1))
