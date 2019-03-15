from math import sqrt, asin, pi
# Note: using only trigonometry is very messy due to floating point errors
# Thus, we will use integrals (which work much nicer in this case)

L = 1.0/4.0 - pi/16.0 # Total area of L-shaped section (let diameter of circle = 1)

def second_integral(n):
    lower_bound = 1.0/(2.0 * sqrt(1.0 + 1.0/n))
    lower = (2.0 * sqrt(1.0-4.0*(lower_bound)**2.0)*lower_bound + asin(2.0*lower_bound))
    upper = asin(1)
    return (1.0/8.0) * (upper - lower)

def compute():
    # Start out at a number so that this will evaluate to True to start
    # This will change in the while loop
    # \int_{0}^{\frac{1}{2 \cdot \sqrt{1 + \frac{1}{n}}}} \frac{x}{n} dx = \frac{1}{8n + 8}
    # \int_{2 \cdot \sqrt{1 + \frac{1}{n}}}}^{\frac{1}{2}} \sqrt{\frac{1}{4} - x^2} dx =
    # \frac{1}{8}\left(2 \cdot \sqrt{1-4 \cdot x^2} x + \arcsin{2x} \right)

    S = L/2
    n = 1
    while S/L >= 0.3646:
        n += 1
        S = 1/(8*n + 8) + second_integral(n)
    return n

if __name__ == '__main__':
    print(compute())