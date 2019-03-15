# Calculate the sum of the first 2 million prime numbers
from math import sqrt
from utils import is_prime


def compute():
    return sum(i for i in range(2, 2_000_001) if is_prime(i))


if __name__ == '__main__':
    print(compute())
