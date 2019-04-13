from math import gcd

LIMIT = 1_000_000

def compute():
    """
    We know that without being exactly equal to 3/7 the 
    largest divisors will be able to approach the closest to 3/7.
    We need to have it within one cycle of 7, because once the modulus of 
    the denominator and 7 repeat, we will be farther away than we were in the greater 
    denominators.
    """
    (num, denom, min_diff) = (0, 1, 3/7)
    for d in range(LIMIT - 7, LIMIT):
        n = int((d / 7) * 3)
        if gcd(n, d) == 1 and 3/7 - n / d < min_diff:
            (num, denom, min_diff) = (n, d, 3/7 - n/d)
    return num

if __name__ == "__main__":
    print(compute())