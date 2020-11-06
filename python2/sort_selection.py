"""
Selection sort.
"""


def selection_sort(A, unused_0=0, unused_1=1):
    for j in range(len(A)-1):
        iMin = j
        for i in range(j+1, len(A)):
            if A[i] < A[iMin]:
                iMin = i
        if iMin != j:
            A[j], A[iMin] = A[iMin], A[j]
