from utils import primes
from utils import is_prime
from itertools import combinations

PRIMES = primes(10000)

def concat_prime(tuple):
    if len(tuple) != 2:
        raise AssertionError("concat_prime requires a tuple with 2 numbers")
    else:
        if is_prime(int(str(tuple[0]) + str(tuple[1]))) and is_prime(int(str(tuple[1]) + str(tuple[0]))):
            return True
        return False

def compute():
    prime_combos = combinations(PRIMES[1:], 2) # 2 cannot be included
    return [v for v in prime_combos if concat_prime(v)][:10]

if __name__ == "__main__":
    print(compute())