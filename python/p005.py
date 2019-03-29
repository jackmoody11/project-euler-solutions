# Find the smallest number that is divisible by the numbers 1, 2, ..., 20
from utils import lcm


def compute():
    # Find the greatest number of prime factors
    # for each prime and multiply them (find the least common multiple).
    # By hand, this gives prod([2**4, 3**2, 5, 7, 11, 13, 17, 19])
    # We will use the lcm function from utils here for clarity
    return lcm(*range(2, 20))


if __name__ == '__main__':
    print(compute())
