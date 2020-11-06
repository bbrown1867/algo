"""
Select the ith smallest element in a given range.
"""

from sort_quick import random_parition


def randomized_select(A, p, r, i):
    if p == r:
        return A[p]
    else:
        q = random_parition(A, p, r)
        # This value is the number of elements in A[p..q]
        k = q - p + 1
        if i == k:
            return A[q]
        elif i < k:
            return randomized_select(A, p, q - 1, i)
        else:
            return randomized_select(A, q + 1, r, i - k)


if __name__ == '__main__':
    A = [11, 0, 1, 2, 500]
    assert randomized_select(A, 0, len(A) - 1, 1) == 0
    assert randomized_select(A, 0, len(A) - 1, 2) == 1
    assert randomized_select(A, 0, len(A) - 1, 3) == 2
    assert randomized_select(A, 0, len(A) - 1, 4) == 11
