def compute():
    """
    Use inclusion-exclusion principle
    """
    return sum(range(3, 1000, 3)) + sum(range(5, 1000, 5)) - sum(range(15, 1000, 15))

if __name__ == "__main__":
    print(compute())