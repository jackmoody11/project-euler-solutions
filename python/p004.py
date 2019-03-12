# Find largest palindrome that is a multiple of 2 3 digit numbers
from utils import is_palindrome

def compute():
    palindromes = []
    for i in range(100, 1000):
        for j in range(100, 1000):
            num = str(i * j)
            if is_palindrome(num):
                palindromes.append((int(i), int(j), int(num)))
    ps = [p[2] for p in palindromes]
    ix = [p[0] for p in palindromes]
    jx = [p[1] for p in palindromes]
    mx = ps.index(max(ps))
    return ix[mx], jx[mx], ps[mx]

if __name__ == '__main__':
    print("Max palindrome: ", compute()[2])
