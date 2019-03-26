#include <stdio.h>

int num_solutions(int p)
{
    int solutions = 0;
    for (long a = 2; a < (p/3); a++) 
    { 
        if (p*(p-2*a) % (2*(p-a)) == 0)
        { 
            solutions++; 
        } 
    }
    return solutions; 
}

int main()
{
    int result = 0;
    int result_solutions = 0;

    for (int p = 2; p <= 1000; p += 2) {
        int p_solutions = num_solutions(p);
        if (p_solutions > result_solutions)
        {
            result_solutions = p_solutions;
            result = p;
        }
    }
    printf("%d\n", result);
}