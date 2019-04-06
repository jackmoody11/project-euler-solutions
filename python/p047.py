# Needs to be optimized further
from utils import primes

CACHE = primes(500_000)

def unique_prime_factors_count(n, x):
    """ Return set of prime factors for integer n. """
    prime_factors = set()
    i = 0
    while n != 1:
        while n % CACHE[i] == 0:
            n /= CACHE[i]
            prime_factors.add(CACHE[i])
        i += 1
        if len(prime_factors) > x:
            return False
    return len(prime_factors) == x


def compute():
    v = 210
    while not all(unique_prime_factors_count(v + i, 4) for i in range(4)):
        v += 1
    return v

if __name__ == "__main__":
    print(compute())