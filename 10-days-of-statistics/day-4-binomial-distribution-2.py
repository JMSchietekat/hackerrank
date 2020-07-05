def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)


def combination(n, x):
    return factorial(n)/(factorial(x) * factorial(n-x))


def binomialProbability(x, n, p):
    # x = number of successes
    # n = total number of trials
    # The probability of success of 1 trial is p.
    # The probability of failure of 1 trial q , where q = 1 - p.

    return combination(n, x) * pow(p, x) * pow((1-p), (n-x))


if __name__ == "__main__":    

    defectivePercentage, batchSize = map(int, input().split())

    binomialDist = 0

    for i in range(0, 3):
        binomialDist += binomialProbability(i, batchSize, defectivePercentage / 100)

    print('{:.3f}'.format(binomialDist))

    binomialDist = 0

    for i in range(2, batchSize+1):
        binomialDist += binomialProbability(i, batchSize, defectivePercentage / 100)

    print('{:.3f}'.format(binomialDist))
