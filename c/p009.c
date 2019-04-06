#include <math.h>
#include <stdio.h>

long find_ab();

int main()
{
    long res = find_ab();
    printf("%ld\n", res);
}

long find_ab()
{
    // Limit of size of a or b
    int limit = 500;
    for (int a = 1; a < limit; a++)
    {
        // Assume that b will be at least as great as a so as not to go over the same a, b combo twice
        for (int b = a; b < limit; b++)
        {
            if (a + b + sqrt(pow(a, 2) + pow(b, 2)) == 1000)
            {
                return (a * b * sqrt(pow(a, 2) + pow(b, 2)));
            }
        }
    }
    return 0;
}