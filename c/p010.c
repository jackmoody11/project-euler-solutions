#include <stdio.h>
#include "utils.h"

int main()
{
    long s = 0;
    for (long i = 2; i <= 2000000; i++)
    {
        if (is_prime(i))
        {
            s += i;
        }
    }
    printf("%ld\n", s);
}