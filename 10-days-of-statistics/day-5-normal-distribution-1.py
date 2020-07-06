import math

def norm_cdf(x, mean, stddev):
	return 0.5 * (1 + math.erf((x - mean) / (stddev * (2 ** 0.5))))


if __name__ == "__main__":

    mean, stddev = map(int, input().split())

    # Less than 19.5
    print('{:.3f}'.format(norm_cdf(19.5, mean, stddev)))
    # Between 20 and 22
    print('{:.3f}'.format(norm_cdf(22, mean, stddev) - norm_cdf(20, mean, stddev)))
