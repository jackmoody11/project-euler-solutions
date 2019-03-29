# Find the smallest number that is divisible by the numbers 1, 2, ..., 20
from utils import prod

def compute():
    # Find the greatest number of prime factors
    # for each prime and multiply them
    # By hand, this gives prod([2**4, 3**2, 5, 7, 11, 13, 17, 19])
    return prod([2**4, 3**2, 5, 7, 11, 13, 17, 19])


if __name__ == '__main__':
    print(compute())
