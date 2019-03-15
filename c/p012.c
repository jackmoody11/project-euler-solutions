#include <stdio.h>
#include <math.h>
#include "utils.h"

int num_divisors(long n);
long tri_500();

int main()
{
    long num = tri_500();
    printf("%d\n", num_divisors(3));
}

int num_divisors(long n)
{
    long end = floor(sqrt(n));
    int result;
    for(long i = 1; i < end + 1; i++)
    {
        if (n % i == 0)
        {
            result += 2;
        }  
    }
    if (pow(end, 2) == n)
    {
        result -= 1;
    }
    return result;
}

long tri_500()
{
    long i = 2;
    long num = 3;
    while(1)
    {
        if (num_divisors(num) > 500) 
        {
            return num;
        }
        else
        {
            i += 1;
            num += i;
        }
    }
}