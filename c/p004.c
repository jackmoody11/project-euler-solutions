#include <stdio.h>
#include "utils.h"

int main()
{
    long num;
    long max_p = 0;
    for(int i = 100; i < 1000; i++)
    {
        for(int j = 100; j < i + 1; j++)
        {
            num = i * j;
            if (is_palindrome(num) && num > max_p) 
            {
                max_p = num;
            }
        }
    }
    printf("%ld\n", max_p);
}