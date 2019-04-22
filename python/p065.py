# Find the sum of digits in the numerator of the 100th convergent of the continued fraction for e.
from utils import digital_sum

def cfrac_to_frac(seq):
    """
    Continued fraction to fraction
    """
    num, den = 1, 0
    for i in reversed(seq):
        num, den = den + num*i, num
    return num, den

def compute():
    e_seq = [2, 1, 2] + [2 * (i + 4) // 3 if i % 3 == 2 else 1 for i in range(97)]
    num = cfrac_to_frac(e_seq)[0]
    return digital_sum(num)

if __name__ == "__main__":
    print(compute())