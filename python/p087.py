from utils import primes
from math import sqrt


def compute():
    LIMIT = 50_000_000
    max_prime = int(sqrt(LIMIT))  # prime**2 must be less than LIMIT
    PRIMES = primes(max_prime)
    numbers = set()
    for x in PRIMES:
        for y in PRIMES:
            for z in PRIMES:
                value = x**2 + y**3 + z**4
                if value < LIMIT:
                    numbers.add(value)
                else:
                    break
    return len(numbers)


if __name__ == "__main__":
    print(compute())
