#include <stdio.h>

// Find the sum of even fibonacci sequences under LIMIT
int LIMIT = 4000000;

int main()
{
    int a = 1;
    int b = 1;
    int a_old;
    int sum = 0;

    while (a <= LIMIT)
    {
        a_old = a;
        a = b;
        b += a_old;
        if (a % 2 == 0)
        {
            sum += a;
        }
    }
    printf("%i\n", sum);
}