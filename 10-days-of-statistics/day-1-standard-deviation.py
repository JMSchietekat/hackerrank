
def mean(x=[]):
    mean = 0

    for i in x:
        mean += i

    return mean / len(x)


def standardDeviation(x=[]):
    u = mean(x)
    stdDev = 0

    for e in x:
        stdDev += pow(e - u, 2)

    return pow(stdDev/len(x), 0.5)


if __name__ == "__main__":

    n = int(input())

    x = list(map(int, input().rstrip().split()))

    print(round(standardDeviation(x), 1))
