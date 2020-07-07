import math


def norm_cdf(x, mean, stddev):
    return 0.5 * (1 + math.erf((x - mean) / (stddev * (2 ** 0.5))))


if __name__ == "__main__":

    x = int(input())
    n = int(input())
    mu = int(input())
    phi = int(input())

    mu_prime = n * mu
    phi_prime = math.sqrt(n) * phi

    # Probability that the elevator can successfully transport all
    print('{:.4f}'.format(norm_cdf(x, mu_prime, phi_prime)))
