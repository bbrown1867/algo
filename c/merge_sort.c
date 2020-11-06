#include <stdio.h>
#include <string.h>
#include <assert.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>

static void merge(int* out, size_t n, int* left, int* right, int mid)
{
    int i = 0;
    int j = 0;
    for (int k = 0; k < n; k++)
    {
        if (i < mid && (j >= mid || left[i] <= right[j]))
        {
            out[k] = left[i];
            i++;
        }
        else
        {
            out[k] = right[j];
            j++;
        }
    }
}

static void mergeSort(int* array, size_t n)
{
    if (n >= 2)
    {
        int mid = n / 2;

        int* left = (int*) malloc(sizeof(mid));
        int* right = (int*) malloc(sizeof(mid));
        memcpy(left, array, sizeof(int) * mid);
        memcpy(right, &array[mid], sizeof(int) * mid);

        mergeSort(left, mid);
        mergeSort(right, mid);
        merge(array, n, left, right, mid);

        free(left);
        free(right);
    }
}

static void mergeSortedArrays(int* arrA, size_t lenA, int* arrB, size_t lenB)
{
    assert(lenB < lenA);

    for (int i = 0; i < lenB; i++)
    {
        arrA[lenA - lenB + i] = arrB[i];
    }

    mergeSort(arrA, lenA);
}

int main(void)
{
    int arrA[] = {1, 2, 3, 4, 6, 8, -1, -1};
    int arrB[] = {5, 7};
    mergeSortedArrays(arrA, 8, arrB, 2);
    for (int i = 0; i < 8; i++)
    {
        assert(arrA[i] == i + 1);
    }

    printf("Passed!\r\n");

    return 0;
}
