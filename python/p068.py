from itertools import permutations

def is_magic(l, n):
    for i in range(n - 1):
        if sum(l[i]) != sum(l[i + 1]) or len(set([i for tup in l for i in tup])) != 2 * n:
            return False
        if any(el > 10 for tup in l for el in tup):
            return False
    return True

def stringify(l):
    return ''.join([str(i) for tup in l for i in tup])

def compute():
    """
    The max smallest node we can have is 6 (we need to force 1 - 5 on the inside).
    Then, the values must equal 6 + a + b where a and b are the nodes on the line of 
    the 6. Going around, we can solve for the outer nodes in terms of 6, a, b, c, d, and e.
    """
    max_combo = '0'
    for (a, b, c, d, e) in tuple(permutations([1,2,3,4,5])):
        triples = [(6, a, b),
                    (6 + a - c, b, c),
                    (6 + a - c + b - d, c, d),
                    (6 + a + b - d - e, d, e),
                    (6 + b - e, e, a)]
        if is_magic(triples, 5) and stringify(triples) > max_combo:
            max_combo = stringify(triples)
            max_triples = triples
    return max_combo

if __name__ == "__main__":
    print(compute())
