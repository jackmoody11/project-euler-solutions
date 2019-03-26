from utils import is_prime
from utils import is_pandigital
from itertools import permutations


def compute():
    max_p = 0
    n = 1
    for i in range(1, 9):
        # Get list of all n pandigitals
        my_str = ""
        for j in range(1, i+1):
            my_str += str(j)
        n_pans = [''.join(p) for p in permutations(my_str)]

        num_n_pan_primes = 0
        for k in n_pans:
            if int(k) > max_p and is_prime(int(k)):
                max_p = int(k)
    return max_p

if __name__ == "__main__":
    print(compute())