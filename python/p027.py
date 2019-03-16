from utils import is_prime

def consecutive_primes(a,b):
    count = 0
    n = 0
    while is_prime(n**2 + a*n + b):
        count += 1
        n += 1
    return count

 
def compute():
    max_consecutive_primes = 0
    coef_product = 0
    for a in range(-1000,1000):
        for b in range(-1001, 1001):
            count = consecutive_primes(a, b)
            if count > max_consecutive_primes:
                coef_product = a * b
                max_consecutive_primes = count
    return coef_product

if __name__ == '__main__':
    print(compute())