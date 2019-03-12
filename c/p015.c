// There are 40 movements (20 downs and 20 rights), so the answer
// is 40 choose 20
#include <stdio.h>
#include <gmp.h>
#include "utils.h"

int main()
{
    mpz_t n, m;

    mpz_init(n);
    mpz_init(m);
    mpz_fac_ui(n, 40);
    mpz_fac_ui(m, 20);
    mpz_mul(m, m, m);
    mpz_divexact(n, n, m);

    mpz_out_str(stdout, 10, n);
    putchar('\n');

    mpz_clear(n);
    mpz_clear(m);

    return 0;
}