from utils import primes, primes_list
from itertools import permutations

PRIMES = primes_list(7)

def follows_pattern(n):
    for i in range(1, 8):
        if int(str(n)[i:i+3]) % PRIMES[i-1] != 0:
            return False
    return True

def compute():
    pattern_sum = 0
    nine_pandigitals = [''.join(p) for p in permutations('0123456789') if p[0] != '0']
    for pandigital in nine_pandigitals:
        if follows_pattern(pandigital):
            pattern_sum += int(pandigital)
    return pattern_sum


if __name__ == "__main__":
    print(compute())