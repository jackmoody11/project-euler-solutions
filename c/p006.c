#include <stdio.h>
#include <math.h>

int main()
{
    int n = 100;
    // \sum_{i=0}^{n} i^2 = \frac{2n^3 + 3n^2 + n}{6}
    // \sum_{i=0}^{n} i = \frac{n(n+1)}{2}
    long diff = pow(((n * (n+1)) / 2), 2) - ((2*pow(n, 3) + 3*pow(n, 2) + n)/ 6);
    printf("%ld", diff);
}