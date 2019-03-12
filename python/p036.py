from utils import is_palindrome


def compute():
    s = 0
    for i in range(1_000_000):
        # bin(585) will return '0b1001001001'
        # only take part after b (2nd index until the end)
        if is_palindrome(str(i)) and is_palindrome(str(bin(i))[2:]):
            s += i
    return s

if __name__ == '__main__':
    print(compute())