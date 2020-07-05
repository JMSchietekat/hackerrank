def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)


def combination(n, x):
    return factorial(n)/(factorial(x) * factorial(n-x))


def binomialProbability(x, n, p):
    return combination(n, x) * pow(p, x) * pow((1-p), (n-x))


if __name__ == "__main__":

    # x = number of successes
    # n = total number of trials
    # The probability of success of 1 trial is p.
    # The probability of failure of 1 trial q , where q = 1 - p .

    b, g = map(float, input().split())

    binomialDist = 0

    for i in range(3, 7):
        binomialDist += binomialProbability(i, 6, b / (b+g))

    print('{:.3f}'.format(binomialDist))
