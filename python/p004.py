# Find largest palindrome that is a multiple of 2 3 digit numbers
from utils import is_palindrome

def compute():
    max_p = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            num = i * j
            if is_palindrome(str(num)) and num > max_p:
                max_p = num
    return max_p

if __name__ == '__main__':
    print("Max palindrome: ", compute())
