# Find 10,001 prime number
from utils import primes_list

def compute():
    return primes_list(10_001)[10_000]

if __name__ == '__main__':
    print(compute())
