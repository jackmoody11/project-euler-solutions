#include <stdio.h>
#include "utils.h"

// Sum all primes <= LIMIT
const int LIMIT = 2000000;

int main()
{
    long s = 0;
    for (long i = 2; i <= LIMIT; i++)
    {
        if (is_prime(i))
        {
            s += i;
        }
    }
    printf("%ld\n", s);
}