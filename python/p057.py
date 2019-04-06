def compute():
    """
    Generalize this by letting a = 2.
    S_{1} = 1 + \frac{1}{a}
    S_{2} = 1 + \frac{1}{(a - 1) + 1 + \frac{1}{a}} = 1 + \frac{1}{S_{1} + (a-1)}
    S_{3} = 1 + \frac{1}{S_{2} + (a-1)}
    ...
    S_{n} = 1 + \frac{1}{S_{n-1} + (a-1)}

    Given that S_{n-1} = \frac{numerator}{denominator}
    S_{n} = 1 + \frac{1}{\frac{numerator}{denominator} + \frac{(a-1) * denominator}{denominator}}
          = 1 + \frac{denominator}{numerator + (a-1) * denominator}
          = \frac{numerator + (a-1) * denominator + denominator}{numerator + (a-1) * denominator}
          = \frac{numerator + a * denominator}{numerator + (a-1) * denominator}
    """
    a = 2 # number being repeated
    count = 0
    iterations = 0
    num = a + 1
    denom = a
    while iterations < 1000:
        if len(str(num)) > len(str(denom)):
            count += 1
        num, denom = (num + a * denom, num + (a - 1) * denom)
        iterations += 1
    return count

if __name__ == "__main__":
    print(compute())