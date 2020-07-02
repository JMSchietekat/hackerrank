
def weightedMean(x=[], weight=[]):
    dividend = 0
    divisor = 0

    assert len(x) == len(
        weight), 'x and weight should have an equal amount of elements'

    for i in range(len(x)):
        dividend += x[i] * weight[i]
        divisor += weight[i]

    return round(dividend / divisor, 1)


if __name__ == "__main__":

    n = int(input())

    x = list(map(int, input().rstrip().split()))
    weight = list(map(int, input().rstrip().split()))

    print(weightedMean(x, weight))
