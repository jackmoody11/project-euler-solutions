# Find largest palindrome that is a multiple of 2 3 digit numbers
from utils import is_palindrome


def compute():
    max_p = 0
    for i in range(100, 1000):
        # Only go to i (inclusive) to eliminate double counting
        for j in range(100, i + 1):
            num = i * j
            if num > max_p and is_palindrome(num):
                max_p = num
    return max_p


if __name__ == '__main__':
    print(compute())
