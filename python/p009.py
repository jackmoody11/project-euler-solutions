# Find a pythagorean triplet such that a^2 + b^2 = c^2, a + b + c = 1000 and a < b < c
# Then print the product a * b * c
from math import sqrt

def compute():
    for a in range(1, 500):
        for b in range(a, 1000):
            if a + b + sqrt(a**2 + b**2) == 1000:
                return a * b * sqrt(a**2 + b**2)

if __name__ == '__main__':
    print(compute())
