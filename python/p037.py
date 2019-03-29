from utils import prime_cache

def is_truncatable_prime(n, cache):
    n_str = str(n)
    for i in range(len(n_str)):
        if cache[int(n_str[i:])] and cache[int(n_str[:i+1])]:
            continue
        else:
            return False
    return True

def compute():
    found = 0
    s = 0
    n = 11 # 2,3,5, and 7 are not truncatable primes
    cache = prime_cache(1_000_000)
    while found != 11:
        if is_truncatable_prime(n, cache):
            found += 1
            s += n
        n += 2
    return s

if __name__ == '__main__':
    print(compute())