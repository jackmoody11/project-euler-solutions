from utils import is_prime

def is_circular(n):
    # If there is an even number in
    # the number, then unless it is 2
    # there will be an even ,and thus
    # non-prime, rotation
    if any((c in ['2','4','6','8']) for c in n):
        return False

    # Check if all rotations are primes
    for i in range(len(n)):
        if is_prime(int(n[i:] + n[:i])):
            continue
        else:
            return False
    return True

def compute():
    # We will not count 2, but start out
    # with one circular prime (2 is circular)
    total = 1
    # If it has an even number, since we already
    # count 2, it won't work
    for i in range(3, 1_000_000, 2):
        if is_circular(str(i)):
            total += 1
    return total

if __name__ == '__main__':
    print(compute())