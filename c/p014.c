#include <stdio.h>

long len_collatz(long n)
{
    int i = 1;
    while(1){
        if (n == 1)
        {
            return i;
        }
        else if (n % 2 == 0)
        {
            n /= 2;
        }
        else
        {
            n = 3 * n + 1;
        }
        i++;
    }  
}

int main()
{
    long max_length = 0;
    long max_n = 0;
    for(int i = 1; i <= 1000000; i++)
    {
        long length = len_collatz(i);
        if (length > max_length)
        {
            max_length = length;
            max_n = i;
        }
    }
    printf("%ld\n", max_n);
}