import math

def isPrime(n):
    if (n < 2):
        return False
    if (n == 2):
        return True
    if (n % 2 == 0):
        return False

	# If a number is divisable by another number less or equal to the square
	# of the first number, it is not prime.

	# This gives a time complexity of (O(sqrt(n)))
    for m in range(3, int(math.sqrt(n))+1, 2):
        if (n % m == 0):
            return False

    return True

if __name__ == "__main__":
    n = int(input())

    for _ in range(n):
        e = int(input())
        print("Prime" if isPrime(e) else "Not prime")