import math

if __name__ == "__main__":

    n = int(input())
    mu = int(input())
    sd = float(input())
    interval = float(input())
    z_score = float(input())

    print('{:.2f}'.format(mu - (sd / math.sqrt(n)) * z_score))
    print('{:.2f}'.format(mu + (sd / math.sqrt(n)) * z_score))
