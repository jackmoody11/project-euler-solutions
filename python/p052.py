def get_digits(x):
    return [int(d) for d in str(x)]


def matches_pattern(x):
    x_sorted_digits = sorted(get_digits(x))
    if all(x_sorted_digits == sorted(get_digits(i * x)) for i in range(2, 7)):
        return True
    return False

def compute():
    x = 1
    while not matches_pattern(x):
        x += 1
    return x

if __name__ == "__main__":
    print(compute())