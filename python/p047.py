def unique_prime_factors(n):
    """ Return set of prime factors for integer n. """
    prime_factors = set()
    i = 2
    # Get prime factors using prime factorization from bottom up (2, 3, 5, ...)
    while i < n**0.5:
        if n % i == 0:
            n /= i
            prime_factors.add(i)
        else:
            i += 1
    return len(prime_factors) + 1


def compute():
    """
    Minimum for j is 2 * 3 * 5 * 7 = 210
    """
    j = 210
    while True:
        
        count = 0
        while unique_prime_factors(j) == 4 and count != 4:
            count += 1
            j += 1
        if count == 4:
            # Added one extra j in loop at the end
            j -= 1
            break
        else:
            j += 1
    return j - 3


if __name__ == "__main__":
    print(compute())