from math import sqrt
from math import factorial
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
    """
    p = 1
    for arg in l:
        p *= arg
    return p

def binom(n, r):
    """Returns 'n choose r'. """
    return (factorial(n) / ((factorial(r) * factorial(n - r))))

def lcm(*nums):
    """
    Find least common multiple of multiple numbers
    >>> lcm(*range(1, 3))
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
    

########################################
################ Primes ################
########################################

def is_prime(n):
    """ Test if integer n is prime. """
    # Negative numbers don't count as primes
    if n < 2:
        return False
    # primes always gives 2 in list, so return True
    # if given n = 2
    elif n == 2:
        return True
    potential_prime_divisors = primes(int(n**0.5) + 1)
    for p in potential_prime_divisors:
        if n % p == 0:
            return False
    return True

def primes_list(n):
    """
    Return first n primes. 
    Different from primes function which returns primes less than n.
    """
    if n == 1:
        return [2]
    elif n == 2:
        return [2, 3]
    prime_count = 2
    i = 5
    p_list = [2, 3]
    while prime_count < n:
        if is_prime(i):
            p_list.append(i)
            prime_count += 1
        i += 2
    return p_list

def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

def prime_cache(n):
    """ True/False list of primes from 0 to n-1 """
    sieve = [False, False] + [True] * (n-2)
    sieve[4::2] = [False] * ((n-3)//2)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return sieve


########################################
############ String Scoring ############
########################################

def word_score(name):
    c_scores = {string.ascii_uppercase[i]: i + 1 for i in range(26)}
    score = 0
    for c in name:
        score += c_scores[c]
    return score


########################################
########## Digit Manipulation ##########
########################################

def is_palindrome(s):
    """ Test whether or not string or int is palindrome """
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
    return set([int(''.join(p)) for p in permutations(str(n)) if p[0] != '0'])

def count_digits(n):
    """ Count digits in positive integer n. """
    count = 0
    while n >= 1:
        count += 1
        n //= 10
    return count

def is_pandigital(n):
    digits = len(n)
    if digits >= 10:
        return False
    string_n = str(n)
    for i in range(1, digits + 1):
        if str(i) not in string_n:
            return False
    return True


########################################
############### Factors ################
########################################

def factors(n):
    """ Return list of prime factors for integer n. """
    potential_factors = primes(n + 1)
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
    # n = (3 * x**2 - x)/2
    # for x to be int, (1 + sqrt(24n + 1)/2 
    # must be int
    pen_test = (1 + sqrt(24*n + 1))/6
    if pen_test == int(pen_test):
        return True
    return False

def is_tri(n):
    # Same reasoning as is_pent
    # means (-1 + sqrt(1 + 8n))/2 must be int
    tri_test = (-1 + sqrt(1 + 8*n))/2
    if tri_test == int(tri_test):
        return True
    return False

def is_hex(n):
    # See tri and pent explanation
    hex_test = (1 + sqrt(1 + 8*n))/4
    if hex_test == int(hex_test):
        return True
    return False
