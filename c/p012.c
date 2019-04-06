// # Find the smallest triangle number that has over five hundred divisors
// # Need to check that this works (is currently taking too long)
#include <math.h>
#include <stdio.h>

int num_divisors(long n);

int main()
{
    long i = 1;
    long num = 1;
    while (num_divisors(num) <= 500)
    {
        i += 1;
        num += i;
    }
    printf("%ld\n", num);
}


int num_divisors(long n)
{
    int res = 0;
    long end = (long) floor(sqrt(n));
    for (long i=1; i < end; i++)
    {
        if (n % i == 0)
        {
            res += 2;
        }
    }
    if (end * end == 2)
    {
        res += 1;
    }
    return res;
}
