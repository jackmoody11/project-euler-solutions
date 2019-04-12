from utils import primes_list, prod

PRIMES = primes_list(10) # we shouldn't need more than 10 primes since 2*3*5*7**6 > 3_000_000
LIMIT = 1_000_000

def compute():
    """
    Euler's Totient function states that \phi(n) = n \prod_{p|n} \left( 1 - \frac{1}{p} \right).
    Therefore, \frac{n}{\phi(n)} = \frac{1}{\prod_{p|n}(1 - \frac{1}{p})}. Note that p is only counted once 
    per occurence, so we want to find the greatest number that can be multiplied by the smallest primes such that 
    it remains under the LIMIT. The smaller the prime, the more that is subtracted from the 1 in the denominator 
    and so the greater the ratio is.
    """
    result = 1
    i = 0
    while result * PRIMES[i] <= LIMIT:
        result *= PRIMES[i]
        i += 1
    return result

if __name__ == "__main__":
    print(compute())