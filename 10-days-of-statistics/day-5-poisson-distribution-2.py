
if __name__ == "__main__":

    lamX, lamY = list(map(float, input().strip().split(' ')))

    # E[X] = lam
    # Var[X] = lam
    # E[X^2] = lam + lam^2

    Ca = 160 + 40 * (lamX + lamX**2)

    print('{:.3f}'.format(Ca))

    Cb = 128 + 40 * (lamY + lamY**2)

    print('{:.3f}'.format(Cb))
