# Find largest palindrome that is a multiple of 2 3 digit numbers
def compute():
    palindromes = []
    for i in range(100, 1000):
        for j in range(100, 1000):
            num = str(i * j)
            if num[:] == num[::-1]:
                palindromes.append((int(i), int(j), int(num)))
    ps = [p[2] for p in palindromes]
    ix = [p[0] for p in palindromes]
    jx = [p[1] for p in palindromes]
    mx = ps.index(max(ps))
    return ix[mx], jx[mx], ps[mx]

if __name__ == '__main__':
    print("i, j, palindrome: ", compute())
    print("Max palindrome: ", compute()[2])
