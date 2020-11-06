/*
 * Find the sum of the first 50,000 prime numbers.
 */

#include <math.h>
#include <stdio.h>
#include <string.h>
#include <assert.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>

static bool is_prime(uint64_t val)
{
    if (val < 2)
    {
        return false;
    }
    else
    {
        for (uint64_t i = 2; i <= (uint64_t) sqrt(val); i++)
        {
            if (val % i == 0ULL)
            {
                return false;
            }
        }

        return true;
    }
}

/* Brute force approach */
static uint64_t sum_of_primes(uint64_t num_primes)
{
    uint64_t idx = 0;
    uint64_t sum = 0;
    uint64_t val = 2;
    while (idx < num_primes)
    {
        if (is_prime(val) == true)
        {
            sum += val;
            idx += 1;
        }

        val += 1;
    }

    return sum;
}

int main(void)
{
    uint64_t sum1 = sum_of_primes(4);
    printf("Sum of the first 4 prime numbers = %llu\r\n", sum1);
    assert(sum1 == 17);

    uint64_t sum2 = sum_of_primes(0);
    printf("Sum of the first 0 prime numbers = %llu\r\n", sum2);
    assert(sum2 == 0);

    uint64_t sum3 = sum_of_primes(50000);
    printf("Sum of the first 50000 prime numbers = %llu\r\n", sum3);

    return 0;
}
