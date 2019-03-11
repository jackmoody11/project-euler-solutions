#include <stdio.h>

int main()
{
    int a = 1;
    int b = 1;
    int limit = 4000000;
    int a_old;
    int sum = 0;

    while (a <= limit)
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