from utils import is_palindrome

def is_lychrel(n, limit):
    count = 0
    while count < limit:
        count += 1
        n_reverse = str(n)[::-1]
        new = n + int(n_reverse)
        if is_palindrome(str(new)):
                return False
        n = new
    return True


def compute():
    return sum(is_lychrel(i, 50) for i in range(1, 10_001))

if __name__ == "__main__":
    print(compute())
