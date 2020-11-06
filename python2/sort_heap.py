"""
Heap sort.
"""

from struct_heap import Heap


def heap_sort(ls, unused_0=0, unused_1=0):
    A = Heap(ls)
    A.max_heap_build()
    for i in reversed(range(1, len(ls))):
        A[0], A[i] = A[i], A[0]
        A.heap_size = A.heap_size - 1
        A.max_heapify()
    return A
