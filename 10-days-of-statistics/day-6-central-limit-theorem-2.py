import math


def norm_cdf(x, mean, stddev):
    return 0.5 * (1 + math.erf((x - mean) / (stddev * (2 ** 0.5))))


if __name__ == "__main__":

    x = int(input())
    n = int(input())
    mu = float(input())
    phi = float(input())

    mu_prime = n * mu
    phi_prime = math.sqrt(n) * phi

    # Probability that 100 students can successfully purchase the remaining 250 tickets
    print('{:.4f}'.format(norm_cdf(x, mu_prime, phi_prime)))
