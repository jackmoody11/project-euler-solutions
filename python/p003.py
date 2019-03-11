# Compute the max prime factor of 600,851,475,143
from math import sqrt


def is_prime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def prime_factors(x):
    max_div = 0
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0 and is_prime(i):
            max_div = i
    return max_div


if __name__ == '__main__':
    print(prime_factors(600851475143))
