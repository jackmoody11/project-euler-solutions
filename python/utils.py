from math import sqrt
from math import factorial
from math import log
from itertools import permutations
from itertools import combinations
from itertools import chain
import string


########################################
############# Basic Math ###############
########################################

def prod(l):
    """
    Takes an iterable and returns product of numbers in iterable.
    Will return 1 if iterable is empty.
    >>> prod(range(1,5))
    24
    >>> prod([2,3,5])
    30
    """
    p = 1
    for arg in l:
        p *= arg
    return p

def binom(n, r):
    """
    Returns 'n choose r'.
    >>> binom(5, 2)
    10
    """
    return factorial(n) // ((factorial(r) * factorial(n - r)))

def lcm(*nums):
    """
    Find least common multiple of multiple numbers
    >>> lcm(*range(1, 4))
    6
    >>> lcm(2,3,4)
    12
    """
    factors_list = [factors(i) for i in nums]
    all_factors = set(chain(*factors_list))
    factor_counts = [{n: fl.count(n) for n in set(fl)} for fl in factors_list]
    result = 1
    for factor in all_factors:
        max_occurences = max([fc.get(factor, 0) for fc in factor_counts])
        result *= factor ** max_occurences
    return result

def is_int(x):
    """
    Returns if a given number is an integer.
    >>> is_int(2.0)
    True
    >>> from math import sqrt; is_int(sqrt(4))
    True
    >>> is_int(5/2)
    False
    """
    return int(x) == x

########################################
################ Primes ################
########################################

def is_prime(n):
    """
    Test if integer n is prime.
    >>> is_prime(25)
    False
    >>> is_prime(11)
    True
    """
    if n < 2:
        return False
    elif n == 2 or n == 3:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, int(sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True

def primes_list(n):
    """
    Return first n primes. 
    Different from primes function.
    >>> primes_list(5)
    [2, 3, 5, 7, 11]

    See https://stackoverflow.com/questions/4911777/finding-first-n-primes
    for source of upper bound
    """
    count = 0
    if n <= 7:
        p_list = [2,3,5,7,11,13,17]
        return p_list[:n]
    else:
        upper_bound = int(n * log(n) + n * log(log(n)))
        return primes(upper_bound)[:n]

def primes(n):
    """
    Returns a list of primes < n
    >>> primes(10)
    [2, 3, 5, 7]
    """
    return [i for i, v in enumerate(prime_cache(n)) if v]

def prime_cache(n):
    """
    True/False list of primes from 0 to n-1
    >>> prime_cache(10)
    [False, False, True, True, False, True, False, True, False, False]
    """
    cache = [False, False] + [True] * (n-2)
    cache[4::2] = [False] * ((n-3)//2)
    for i in range(3,int(n**0.5)+1,2):
        if cache[i]:
            cache[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return cache

def phi(n, cache=None):
    """
    Returns number of natural numbers which are less than and relatively prime to n.
    >>> phi(2)
    1
    >>> phi(7)
    6
    """
    if n == 1:
        return 1
    elif n < 1:
        raise AssertionError('Please enter an int > 0')
    else:
        return int(n * prod([1 - 1/p for p in set(factors(n, cache))]))

def list_totients(n):
    """
    List of totients up to n, inclusive.
    Used from nayuki's eulerlib.
    https://github.com/nayuki/Project-Euler-solutions/blob/master/python/eulerlib.py
    """
    results = list(range(n + 1))
    for i in range(2, len(results)):
        if results[i] == i:
            for j in range(i, len(results), i):
                results[j] -= results[j] // i
    return results

def farey(n, a=None, b=None, c=None, d=None):
    """Print the nth Farey sequence, ascending."""
    pairs = []
    if any(i is None for i in (a,b,c,d)):
        a, b, c, d = 1, n, 1, n-1
    pairs.append((a,b))
    while c <= n:
        k = int((n + b) / d)
        a, b, c, d = c, d, (k*c-a), (k*d-b)
        pairs.append((a,b))
    return pairs

def farey_count(n, a, b, num, denom):
    """Find number of proper fractions for b <= n in between a/b and num/denom"""
    count = 0
    c, d = n / b, n - 1
    while c != num and d != denom:
        k = int((n + b) / d)
        a, b, c, d = c, d, (k*c-a), (k*d-b)
        count += 1
    return count


########################################
############ String Scoring ############
########################################

def word_score(name):
    """
    Map letters to scores {'A': 1, 'B': 2, ..., 'Z': 26}.
    Upper and lowercase both receive same score.
    >>> word_score('a')
    1
    >>> word_score('Python')
    98
    """
    c_scores = {string.ascii_uppercase[i]: i + 1 for i in range(26)}
    score = 0
    for c in name.upper():
        score += c_scores[c]
    return score


########################################
########## Digit Manipulation ##########
########################################

def is_palindrome(s):
    """
    Test whether or not string or int is palindrome
    >>> is_palindrome(121)
    True
    >>> is_palindrome(125)
    False
    >>> is_palindrome('121')
    True
    """
    if isinstance(s, str):
        if s == s[::-1]:
            return True
        else:
            return False
    if isinstance(s, int):
        if str(s) == str(s)[::-1]:
            return True
        else:
            return False
    else:
        raise AssertionError("Please enter str")

def digit_permutations(n):
    """
    Find all permutations of digits of number. 
    Permutation cannot start with 0 unless n = 0.
    >>> digit_permutations(123) == {321, 132, 231, 213, 312, 123}
    True
    >>> digit_permutations(11) == {11}
    True
    >>> digit_permutations(10) == {10}
    True
    """
    if n != 0:
        return set([int(''.join(p)) for p in permutations(str(n)) if p[0] != '0'])
    else:
        return {0}

def count_digits(n):
    """
    Count digits in positive integer n.
    >>> count_digits(125)
    3
    >>> count_digits(2)
    1
    """
    return len(str(n))

def is_pandigital(n):
    """
    Returns whether number is pandigital
    >>> is_pandigital('123')
    True
    >>> is_pandigital('1232')
    False
    """
    # Accept both str and int
    if isinstance(n, int):
        n = str(n)

    digits = len(n)
    if digits >= 10:
        return False
    string_n = str(n)
    for i in range(1, digits + 1):
        if str(i) not in string_n:
            return False
    return True

def is_permutation(a, b):
    if sorted(str(a)) == sorted(str(b)):
        return True
    else:
        return False

def digital_sum(n):
    """
    Returns sum of digits of integer
    >>> digital_sum(123)
    6
    """
    r = 0
    while n:
       r, n = r + n % 10, n // 10
    return r


########################################
############### Factors ################
########################################

def factors(n, cache=None):
    """
    Return list of prime factors for integer n.
    >>> factors(35)
    [5, 7]
    >>> factors(24)
    [2, 2, 2, 3]
    """
    if cache is None or max(cache) < n:
        potential_factors = primes(n + 1)
    else:
        potential_factors = cache
    prime_factors = []
    i = 0
    while n != 1:
        while n % potential_factors[i] == 0:
            n /= potential_factors[i]
            prime_factors.append(potential_factors[i])
        i += 1
    return prime_factors


########################################
############### Sequences ##############
########################################

def is_pent(n):
    """
    n = (3 * x**2 - x)/2
    for x to be int, (1 + sqrt(24n + 1)/2 
    must be int
    >>> is_pent(5)
    True
    >>> is_pent(6)
    False
    """
    pen_test = (1 + sqrt(24*n + 1))/6
    if pen_test == int(pen_test):
        return True
    return False

def is_tri(n):
    """
    Same reasoning as is_pent
    means (-1 + sqrt(1 + 8n))/2 must be int
    >>> is_tri(3)
    True
    >>> is_tri(5)
    False
    """
    tri_test = (-1 + sqrt(1 + 8*n))/2
    if tri_test == int(tri_test):
        return True
    return False

def is_hex(n):
    """
    Test if number is hexagonal number.
    That is, of the form 2n * (2n-1)/2.
    >>> is_hex(6)
    True
    >>> is_hex(11)
    False
    """
    hex_test = (1 + sqrt(1 + 8*n))/4
    if hex_test == int(hex_test):
        return True
    return False
