"""
Counting based sorting algorithms.
"""

import math
from struct_linkedlist import LinkedList


def counting_sort(A, unused_0=0, unused_1=0):
    """
    Unlike the book, we don't require the max value be passed in and just find
    it using "max". We also just create the output array B locally instead of
    passing it in.
    """
    k = max(A) + 1
    B = [0 for i in range(len(A))]
    C = [0 for i in range(k)]

    for j in range(len(A)):
        C[A[j]] = C[A[j]] + 1

    for i in range(1, k):
        C[i] = C[i] + C[i - 1]

    for j in reversed(range(len(A))):
        # Subtract 1 because we go from [0, length - 1] not [1, length]
        B[C[A[j]] - 1] = A[j]
        C[A[j]] = C[A[j]] - 1

    return B


def radix_sort(B, unused_0=0, unused_1=1):
    """
    Unlike the book, determine number of digits locally instead of passing d.
    """
    d = []
    for b in B:
        d.append(int(math.floor(math.log10(b))))
    if all(x == d[0] for x in d):
        d = d[0]
    else:
        raise Exception('All elements must have same number of digits')

    for i in reversed(range(d + 1)):
        st_B = []
        for b in B:
            s = str(b)
            # What the hell is going on? str.split not working
            st = []
            for c in s:
                st.append(c)
            st_B.append(st)

        st_B.sort(key=lambda st: int(st[i]))

    for i in range(len(B)):
        B[i] = int("".join(st_B[i]))

    return B


def bucket_sort(A):
    """
    Assume A is evenly distributed over the range [0, 1).
    """
    B = []
    for i in range(len(A)):
        B.append(LinkedList())

    for a in A:
        index = int(math.floor(len(A)*a))
        B[index].insert(a)

    for b in B:
        b.sort()

    ls = []
    for b in B:
        ls.append(b.convert_to_list())

    return [item for sub_ls in ls for item in sub_ls]


if __name__ == '__main__':
    A = [329, 457, 657, 839, 436, 720, 355]
    B = radix_sort(A)
    print(B)

    A = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
    B = bucket_sort(A)
    print(B)
