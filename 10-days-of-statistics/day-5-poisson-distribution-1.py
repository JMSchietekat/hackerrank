def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)


def poissonProbability(k, lam):
    # lamda is the average number of successes that occur in a specified region.
    # k is the actual number of successes that occur in a specified region.

    return (pow(lam, k) * pow(2.71828, -lam))/factorial(k)


if __name__ == "__main__":

    lam = float(input())
    k = int(input())

    print('{:.3f}'.format(poissonProbability(k, lam)))
