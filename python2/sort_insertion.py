"""
Insertion sort.
"""


def insertion_sort(A, unused_0=0, unused_1=1):
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i > -1 and A[i] > key:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key
