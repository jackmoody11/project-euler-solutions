from math import factorial
# nCr = n! / r! (n - r)!
# We want n! > 1,000,000 * r! * (n-r)!

def ncr_exceeds_million(n, r):
    if r >= n:
        raise Exception("n must be greater than r")
    if factorial(n) > 1_000_000 * factorial(r) * factorial(n - r):
        return True
    return False

def compute():
    return sum([1 for n in range(23, 101) for r in range(0, n) if ncr_exceeds_million(n, r)])

if __name__ == "__main__":
    print(compute())
    