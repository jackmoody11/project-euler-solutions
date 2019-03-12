#include <stdio.h>
#include <math.h>

int main()
{
    int n = 100;
    long diff = pow(((n * (n+1)) / 2), 2) - ((2*pow(n, 3) + 3*pow(n, 2) + n)/ 6);
    printf("%ld", diff);
}