def IQR(x):
    q = quartiles(s)

    return (q[2] - q[0])


def median(x=[]):
    x.sort()
    x_cnt = len(x)

    if(x_cnt % 2 == 0):
        return (x[int(x_cnt/2) - 1] + x[int(x_cnt/2)])/2
    else:
        return x[int(x_cnt/2)]


def quartiles(x=[]):
    x.sort()
    q2 = median(x)

    setCnt = len(x)

    if(setCnt % 2 == 0):
        q1 = median(x[:int(setCnt/2)])
        q3 = median(x[int(setCnt/2):])
    else:
        q1 = median(x[:int(setCnt/2)])
        q3 = median(x[int(setCnt/2)+1:])

    return q1, q2, q3

def flattenSet(x, f):
    s = []

    for i, v in enumerate(x):
        for _ in range(f[i]):
            s.append(v)

    return s

if __name__ == "__main__":

    n = int(input())

    x = list(map(int, input().rstrip().split()))
    f = list(map(int, input().rstrip().split()))

    s = flattenSet(x,f)

    print(round(IQR(s) * 1.0, 1))
