from utils import is_prime

def is_truncatable_prime(n):
    n_str = str(n)
    for i in range(len(n_str)):
        if is_prime(int(n_str[i:])) and is_prime(int(n_str[:i+1])):
            continue
        else:
            return False
    print(n)
    return True

def compute():
    found = 0
    s = 0
    n = 11 # 2,3,5, and 7 are not truncatable primes
    while found != 11:
        if is_truncatable_prime(n):
            found += 1
            s += n
        n += 1
    return s

if __name__ == '__main__':
    print(is_truncatable_prime(11))
    print(compute())