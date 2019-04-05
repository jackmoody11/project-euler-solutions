from collections import Counter

# Given that 345 is smallest cube that has 3 cube permutations
# Will guess that we will not go past 10_000 ** 3
# If none were found, this could be increased further, but to save computing
# time it is limited to 10_000
CUBES = [''.join(sorted(str(i**3))) for i in range(345, 10_000)]

def is_permutation(a, b):
    if len(a) == len(b) and Counter(a) == Counter(b):
        return True
    return False

def compute():
    # Count number of each permutation
    counter = Counter(CUBES)
    perms = []
    for k, v in counter.items():
        if counter[k] == 5:
            perms.append(k)
    
    # Only take the permutations with the smallest num. of digits
    req_len = len(min(perms, key=len))
    perms = [p for p in perms if len(p) == req_len]
    # Check for i such that i**3 goes from just below the minimum value of the permutation
    # to just above the maximum possible value of the permutation
    start = int(int(perms[0])**(1/3))
    end = int(int(perms[0][::-1])**(1/3))
    # Search for smallest cube that creates permutation
    for i in range(start, end + 1):
        if is_permutation(str(i**3), perms[0]):
            return i**3

if __name__ == "__main__":
    print(compute())