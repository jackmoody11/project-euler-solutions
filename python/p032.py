from utils import is_pandigital

def is_nine_pandigital_product(a, b):
    my_str = str(a) + str(b) + str(a*b)
    if len(my_str) == 9 and is_pandigital(my_str):
        return True
    else:
        return False

def compute():
    # 1 will never return a pandigital product (will repeat digits)
    pandigitals = set()
    # sqrt(987654321) = 31426.96, so we know this is the
    # upper limit for our larger number (we define b as the larger number here)
    for a in range(2, 31426):
        for b in range(a, 31426):
            mult = a * b
            if len(str(a) + str(b) + str(mult)) > 9:
                # Once the concatenation of a, b, and a + b gives
                # a string of length > 9, we can skip to the next 
                # value for a
                break
            if is_nine_pandigital_product(a, b) and mult not in pandigitals:
                pandigitals.add(mult)
    return sum(pandigitals)

if __name__ == "__main__":
    print(compute())