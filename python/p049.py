from itertools import combinations, permutations
from utils import is_prime


def follows_pattern(n):
    prime_perms = list(filter(lambda x: is_prime(int(x)), [''.join(p) for p in permutations(n)]))
    combo_triplets = list(combinations(prime_perms, 3))
    combo_triplets.sort()
    if combo_triplets:
        for tup in combo_triplets:
            if int(tup[2]) - int(tup[1]) == int(tup[1]) - int(tup[0]) != 0:
                return (True, tup)
    return (False, (0))

def compute():
    combo_str = '123456789' * 4
    # Get rid of repeated numbers in combinations
    combos = list(set([''.join(c) for c in combinations(combo_str,4)]))
    # Get rid of repeated permutations
    combos = list(set([''.join(sorted(a)) for a in combos]))
    for combo in combos:
        # Don't print 1487 number - we already knew about that one
        if follows_pattern(combo)[0] and combo not in list(''.join(p) for p in permutations('1487')):
            return "".join(follows_pattern(combo)[1])

if __name__ == "__main__":
    print(compute())