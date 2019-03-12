#include <stdio.h>
#include <math.h>

#include "utils.h"

int main()
{
    long max_div = max_prime_factor(600851475143);
    printf("%ld\n", max_div);
}