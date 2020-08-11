import time


def timeConversion(s):
    time_obj = time.strptime(s, "%I:%M:%S%p")
    return time.strftime("%H:%M:%S", time_obj)


if __name__ == '__main__':
    s = input()

    print(timeConversion(s))
