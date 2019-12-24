from math import log


def read_values():
    values = []
    with open('p099.txt', 'r') as f:
        for line in f:
            values.append(tuple(map(int, line.strip('\n').split(','))))
    return values


def compute():
    """ Uses fact that log is monotonically increasing for positive numbers and 
    log(a**b) = b * log(a). """
    pairs = read_values()
    max_value_line = 0
    max_value = 0
    for i in range(len(pairs)):  # counts line 1 as 0, need to add 1 to end result
        log_value = pairs[i][1] * log(pairs[i][0])
        if log_value > max_value:
            max_value = log_value
            max_value_line = i
    return max_value_line + 1  # starts indexing at 0, so must add 1 to compensate


if __name__ == "__main__":
    print(compute())
