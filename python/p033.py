from math import gcd

def is_curious(a, b):
    orig_frac = a / b
    if a % 10 == 0 or b % 10 == 0:
        return False
    # Let sa and sb be the string versions of a and b
    sa, sb = str(a), str(b)
    # Check if any of the combinations give curious fractions
    if sa[0] == sb[0] and orig_frac == int(sa[1]) / int(sb[1]):
        return True
    if sa[0] == sb[1] and orig_frac == int(sa[1]) / int(sb[0]):
        return True
    if sa[1] == sb[0] and orig_frac == int(sa[0]) / int(sb[1]):
        return True
    if sa[1] == sb[1] and orig_frac == int(sa[0]) / int(sb[0]):
        return True
    return False

def compute():
    # a < b since we are given that a/b < 1
    num, denom = 1, 1
    for a in range(11, 100):
        for b in range(a+1, 100):
            if is_curious(a, b):
                num *= a
                denom *= b
    return int(denom / gcd(num, denom))
    

if __name__ == "__main__":
    print(compute())