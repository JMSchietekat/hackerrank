
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


if __name__ == "__main__":

    n = int(input())

    elem = list(map(int, input().rstrip().split()))

    quartiles = quartiles(elem)

    print(int(quartiles[0]))
    print(int(quartiles[1]))
    print(int(quartiles[2]))
