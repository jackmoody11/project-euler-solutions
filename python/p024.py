# Lucky for us, python itertools does this really well!
from itertools import permutations

def compute():
    perms = list(map("".join, permutations('0123456789')))
    return perms[999999]

if __name__ == '__main__':
    print(compute())