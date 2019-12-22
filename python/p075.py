from math import gcd, sqrt
""" All primitive pythagorean triples can be formed by finding 
    s, t \in \Z such that s > t, gcd(s, t) = 1, and s \not\equiv t \mod(2).
    Given any s, t satisfying these conditions, a^2 + b^2 = c^2 where 
    a = 2st, b = s^2 - t^2, c = s^2 + t^2."""


def _get_coprime_combos(s, limit):
    """ Returns all combos of s and another number up to limit 
        such that s and t can help make primitive Pythagorean 
        triangle. """
    combos = []
    if s < 1:
        raise ValueError("s should be greater than 1")
    if s % 2 == 0:
        start = 1
    else:
        start = 2
    for t in range(start, s, 2):  # s and t must be opposite parity, so step by 2
        if gcd(s, t) == 1 and (s + t) % 2 == 1:
            combos += [(s, t)]
    return combos


def get_s_t_combos(s_limit):
    """ Get all combos of s and t that will make primitive 
        Pythagorean triangle such that s > t, s \not\equiv t \mod(2),
        and \gcd(s, t) = 1. 
    """
    all_combos = []
    for s in range(2, s_limit + 1):
        all_combos += _get_coprime_combos(s, 1_500_000)
    return all_combos


def get_primitive_ls(s_t_combos):
    """ Get all lengths of triangles given by primitive Pythagorean 
        triples.
    """
    return [2*s**2 + 2*s*t for s, t in s_t_combos]


def get_lcount(primitive_ls):
    """ Get number of triples that sum to make 
        total length of triangle equal to l.
        If a^2 + b^2 = c^2 for a, b, c \in \Z_{>0}, then 
        l = a + b + c.
    """
    l_count = [0] * 1_500_001
    for l in primitive_ls:
        l_count[l::l] = [v + 1 for v in l_count[l::l]]
    return l_count


def count_unique_ls(primitive_ls):
    """ Count number of lengths l where there is only one way such 
        that a, b, c \in \Z, a^2 + b^2 = c^2, and a + b + c = l.
    """
    return sum([count == 1 for count in get_lcount(primitive_ls)])


def compute():
    s_t_combos = get_s_t_combos(s_limit=int(sqrt(1_500_000/2)))
    primitive_ls = get_primitive_ls(s_t_combos)
    l_count = get_lcount(primitive_ls)
    return count_unique_ls(primitive_ls)


if __name__ == "__main__":
    print(compute())
