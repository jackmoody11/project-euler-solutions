# Compute the max prime factor of 600,851,475,143
# It is easily verified that 71 is the 
# smallest prime divisor, and thus we only need to check
# to sqrt of the number (it is not prime itself)
from math import sqrt
from utils import is_prime
    
TARGET = 600_851_475_143 

def compute():
    max_div = 0
    for i in range(2, int(sqrt(TARGET)) + 1):
        if TARGET % i == 0 and is_prime(i):
            max_div = i
    return max_div

if __name__ == '__main__':
    print(compute())
