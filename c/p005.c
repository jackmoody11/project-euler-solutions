#include <stdio.h>
#include <math.h>

int is_divisible_up_to(long x, int n);

int main()
{
    long x = 2520;
    while(!is_divisible_up_to(x, 20)){
        x += 20;
    }
    printf("%ld\n", x);
    
}

int is_divisible_up_to(long x, int n)
{
    for(int i = 2; i <= n; i++)
    {
        if (x % i != 0) {
            return 0;
        }  
    }
    return 1; 
}