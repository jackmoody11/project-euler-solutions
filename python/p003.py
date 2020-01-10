# Compute the max prime factor of 600,851,475,143
# It is easily verified that 71 is the
# smallest prime divisor, and thus we only need to check
# to sqrt of the number (it is not prime itself)
from math import sqrt
from utils import is_prime, primes


def compute():
    TARGET = 600_851_475_143
    PRIMES = primes(int(sqrt(TARGET)) + 1)
    max_div = 0
    for p in PRIMES:
        if TARGET % p == 0:
            max_div = p
        while TARGET % p == 0:
            TARGET //= p
    if TARGET > max_div:
        return TARGET
    else:
        return max_div


if __name__ == '__main__':
    print(compute())
