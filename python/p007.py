# Find 10,001 prime number
from utils import is_prime


def nth_prime(n):
    count = 0
    number = 1
    while count < n:
        number += 1
        if is_prime(number):
            count += 1
    return number


if __name__ == '__main__':
    print(nth_prime(10_001))
