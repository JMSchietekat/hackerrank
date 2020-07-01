
def weightedMean(elem=[], weight=[]):
    dividend = 0
    divisor = 0

    assert len(elem) == len(
        weight), 'elem and weight should have an equal amount of elements'

    for i in range(len(elem)):
        dividend += elem[i] * weight[i]
        divisor += weight[i]

    return round(dividend / divisor, 1)


if __name__ == "__main__":

    n = int(input())

    elem = list(map(int, input().rstrip().split()))
    weight = list(map(int, input().rstrip().split()))

    print(weightedMean(elem, weight))
