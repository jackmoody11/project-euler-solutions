#include <stdio.h>
#include "utils.h"

int main()
{
    int p = 0;
    long x = 1;
    while(p < 10001){
        x += 1;
        if (is_prime(x)) {
            p += 1;
        }
    }
    printf("%ld\n", x);
}