from math import ceil, floor

def n_digit_numpow(n):
    """
    Returns number of integers j where 
    j**n is an n-digit number.
    >>> n_digit_numpow(1)
    9
    >>> n_digit_numpow(2)
    6
    """
    count = 0
    if n < 1:
        raise ValueError("n must be >= 1")
    elif n == 1:
        return 9
    else:
        lower_bound = int('9'*(n-1))
        for j in range(ceil(lower_bound**(1/n)), ceil(10*10**(1/n))):
            if j**n < 10**n and lower_bound < j**n:
                count += 1
    return count

def compute():
    count = 0
    n = 1
    while n_digit_numpow(n) > 0:
        count += n_digit_numpow(n)
        n += 1
    return count

if __name__ == "__main__":
    print(compute())