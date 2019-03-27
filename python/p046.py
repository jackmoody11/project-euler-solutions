from utils import is_prime, prime, primes
from math import sqrt

def compute():
    # We are given that this pattern holds at least until 33
    prime_list_full = primes(10000)
    num = 35
    while True:
        prime_list = [p for p in prime_list_full if p < num]
        if not (any(sqrt(num/2 - p/2) == int(sqrt(num/2 - p/2)) for p in prime_list)) and not is_prime(num):
            return num
        num += 2    


if __name__ == "__main__":
    print(compute())