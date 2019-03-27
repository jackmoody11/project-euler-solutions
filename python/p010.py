# Calculate the sum of the first 2 million prime numbers
from math import sqrt
from utils import primes


def compute():
    return sum(primes(2_000_001))


if __name__ == '__main__':
    print(compute())
