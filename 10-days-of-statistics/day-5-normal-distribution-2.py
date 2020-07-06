import math

def norm_cdf(x, mean, stddev):
	return 0.5 * (1 + math.erf((x - mean) / (stddev * (2 ** 0.5))))


if __name__ == "__main__":

    mean, stddev = map(int, input().split())

    # Scored higher than 80
    print('{:.2f}'.format((1 - norm_cdf(80, mean, stddev)) * 100))
    # Passed the test grade >= 60
    print('{:.2f}'.format((1 - norm_cdf(60, mean, stddev)) * 100))
    # Failed the test < 60
    print('{:.2f}'.format(norm_cdf(60, mean, stddev) * 100))
