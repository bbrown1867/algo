/*
 * Randomly select K elements from the range [0:N).
 */

#include <math.h>
#include <stdio.h>
#include <string.h>
#include <assert.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>

/* Fisher–Yates shuffle */
static void random_select(int* pool, size_t n, int* result, size_t k)
{
    for (int i = 0; i < k; i++)
    {
        int idx = i + (rand() % (n - i));

        /* Swap */
        int tmp = pool[i];
        pool[i] = pool[idx];
        pool[idx] = tmp;
    }

    /* First k elements of pool are random */
    memcpy((void*) result, (void*) pool, k * sizeof(int));
}

int main(void)
{
    const int k_size = 10;
    const int n_size = 50;

    int* pool = (int*) malloc(n_size * sizeof(int));
    int* elem = (int*) malloc(k_size * sizeof(int));

    for (int i = 0; i < n_size; i++)
    {
        pool[i] = i;
    }

    random_select(pool, n_size, elem, k_size);

    for (int i = 0; i < k_size; i++)
    {
        printf("%d: %d\r\n", i, elem[i]);
    }
}
