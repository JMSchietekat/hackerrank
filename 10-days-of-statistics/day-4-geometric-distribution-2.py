def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)


def combination(n, x):
    return factorial(n)/(factorial(x) * factorial(n-x))


def negativeBinomialProbability(x, n, p):
    # x = number of successes
    # n = total number of trials
    # The probability of success of 1 trial is p.
    # The probability of failure of 1 trial q , where q = 1 - p.

    return combination(n - 1, x - 1) * pow(p, x) * pow((1-p), (n-x))


def geometricProbability(n, p):
    return negativeBinomialProbability(1, n, p)


if __name__ == "__main__":

    numerator, denominator = map(int, input().split())
    n = int(input())

    p = numerator / denominator

    gb = 0

    for i in range(1, n+1):
        gb += geometricProbability(i, p)

    print('{:.3f}'.format(gb))
