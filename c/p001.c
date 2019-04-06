#include <stdio.h>

// Sum divisors of 3 or (inclusive) 5 up to LIMIT
const int LIMIT = 1000;

int main()
{
    int sum = 0;

    for (int i = 0; i < LIMIT; i++)
    {
        if (i % 3 == 0 || i % 5 == 0)
        {
            sum += i;
        }
    }
    printf("%i\n", sum);
}