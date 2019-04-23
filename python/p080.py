from decimal import getcontext, Decimal

def compute():
    getcontext().prec = 102 # Set accuracy to 102 places (extra 2 for whole number part)
    LIMIT = 100
    not_square = [i for i in range(LIMIT + 1) if int(i**0.5) != i**0.5]

    return sum(
        (sum(Decimal(i).sqrt().as_tuple().digits[:100]) for i in not_square)
    )
    


if __name__ == "__main__":
    print(compute())
