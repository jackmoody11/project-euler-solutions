# Find 10,001 prime number
from math import sqrt


def is_prime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def nth_prime(n):
    p = 0
    x = 1
    while p < n:
        x += 1
        if is_prime(x):
            p += 1
    return x


if __name__ == '__main__':
    print(nth_prime(10_001))
