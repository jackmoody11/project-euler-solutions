# Calculate the sum of the first 2 million prime numbers
from math import sqrt


def is_prime(n):
    if n == 1:
        return False
    if n == 2 or n == 3:
        return True
    else:
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
    return True


def compute():
    s = 0
    for i in range(2, 2_000_001):
        if is_prime(i):
            s += i
    return s


if __name__ == '__main__':
    print(compute())
