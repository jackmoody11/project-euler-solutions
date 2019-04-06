#include <stdio.h>
#include <math.h>

#include "utils.h"

// Find max prime factor of NUM
long NUM = 600851475143;

int main()
{
    long max_div = max_prime_factor(NUM);
    printf("%ld\n", max_div);
}