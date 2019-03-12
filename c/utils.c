#include <math.h>
#include "utils.h"

int is_prime(int n)
{
    if (n < 2)
    {
        return 0;
    }
    int last = (int) sqrt(n) + 1;  /* conservatively safe */

    for (int j = 2; j <= last; ++j)
    {
        if (0 == n % j)
        {
        return 0;
        }
    }
  return 1;
}

long max_prime_factor(long n)
{
    long max_possible = (long) sqrt(n) + 1;
    long max_div;
    for(long i = 2; i <= max_possible; i++)
    {
        if (n % i == 0 && is_prime(i)) 
        {
            max_div = i;
        }
    }
    return max_div;
    
}