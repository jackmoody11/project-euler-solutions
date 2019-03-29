from utils import factors

def unique_prime_factors(n):
    return [len(set(factors(i))) for i in range(1, n)]


def compute():
    num_prime_factors = unique_prime_factors(1_000_000)
    for idx, val in enumerate(num_prime_factors):
        if all(num_prime_factors[idx + j] == 4 for j in range(4)):
            return idx + 1

if __name__ == "__main__":
    print(compute())