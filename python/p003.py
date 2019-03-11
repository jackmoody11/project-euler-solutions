# Compute the max prime factor of 600,851,475,143
from math import sqrt


def is_prime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def prime_factors(x):
    divs = []
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0 and is_prime(i):
            divs.append(i)
    return divs


if __name__ == '__main__':
    print(max(prime_factors(600851475143)))
