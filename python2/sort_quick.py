"""
Quick sort.
"""

import random


def partition(A, p, r):
    pivot = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= pivot:
            i = i + 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return (i + 1)


def hoare_partition(A, p, r):
    pivot = A[p]
    i = p - 1
    j = r + 1
    while True:
        while True:
            j = j - 1
            if A[j] <= pivot:
                break
        while True:
            i = i + 1
            if A[i] >= pivot:
                break
        if i < j:
            A[i], A[j] = A[j], A[i]
        else:
            return j


def random_parition(A, p, r):
    i = random.randint(p, r)
    A[i], A[r] = A[r], A[i]
    return partition(A, p, r)


def quick_sort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q - 1)
        quick_sort(A, q + 1, r)


def hoare_quick_sort(A, p, r):
    if p < r:
        q = hoare_partition(A, p, r)
        hoare_quick_sort(A, p, q)
        hoare_quick_sort(A, q + 1, r)


def random_quick_sort(A, p, r):
    if p < r:
        q = random_parition(A, p, r)
        random_quick_sort(A, p, q - 1)
        random_quick_sort(A, q + 1, r)
