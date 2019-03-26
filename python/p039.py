def num_solutions(p):
    count = 0
    for a in range(2, p//3):
        # Know that b must be (p**2 - 2*a*p) / (2*(p - a))
        # by solving a**2 = b**2 = (p - a - b)**2
        # Therefore, for b to be an integer,
        #  (p**2 - 2*a*p) % (2*(p - a)) == 0
        if (p**2 - 2*a*p) % (2*(p - a)) == 0:
            count += 1
    return count

def compute():
    max_p = (0, 0) # (p, # of solutions)
    # If one of a or b is odd, c is odd => p is even
    # If both a and b are odd, c is even => p is even
    # If a and b are both even, c is even => p is even
    for p in range(12, 1001, 2):
        sols = num_solutions(p)
        if sols > max_p[1]:
            max_p = (p, sols)
    return max_p[0]

if __name__ == "__main__":
    print(compute())
