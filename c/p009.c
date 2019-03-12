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
    for (int a = 1; a < 500; a++)
    {
        for (int b = 1; b < 500; b++)
        {
            if (a + b + sqrt(pow(a, 2) + pow(b, 2)) == 1000)
            {
                return (a * b * sqrt(pow(a, 2) + pow(b, 2)));
            }
        }
    }
    return 0;
}