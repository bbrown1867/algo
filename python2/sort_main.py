"""
Test harness for sorting algorithms.
"""

import time
import random
from tabulate import tabulate
from sort_heap import heap_sort
from sort_merge import merge_sort
from sort_counting import counting_sort
from sort_selection import selection_sort
from sort_insertion import insertion_sort
from sort_quick import quick_sort, hoare_quick_sort, random_quick_sort


def timing(func):
    """
    Function decorator for timing a function, not good for recursion.
    """
    def wrap(*args):
        time1 = time.time()
        ret = func(*args)
        time2 = time.time()
        dbg = func.func_name, (time2 - time1) * 1000.0
        print("%s function took %0.3f ms" % dbg)
        return ret
    return wrap


def unit_test_sorting(func, *args):
    """
    Unit testing, but only for sorting functions.
    """
    out = func(*args)
    if out is None:
        out = args[0]
    exp = sorted(args[0])
    if out != exp:
        print("Test Failed: " + func.func_name)
        print("Expected = " + str(exp))
        print("Actual = " + str(out))
        exit(1)

    return out


def stress_test_sorting(func):
    num_vals = 500

    # Test with already sorted array
    time1 = time.time()
    func(range(num_vals), 0, num_vals - 1)
    time2 = time.time()
    best = (time2 - time1)*1000.0

    # Test with perfectly unsorted array
    time1 = time.time()
    func(list(reversed(range(num_vals))), 0, num_vals - 1)
    time2 = time.time()
    worst = (time2 - time1)*1000.0

    # Test with random array
    time1 = time.time()
    func([random.randint(0, num_vals) for _ in range(num_vals)],
         0, num_vals - 1)
    time2 = time.time()
    rando = (time2 - time1)*1000.0

    # Print results
    print(tabulate([['Best', best], ['Worst', worst], ['Random', rando]],
                   headers=[func.func_name, 'Time (ms)']))
    print('\r\n')


def refresh_tests():
    """
    In place sorting will muck up the test vectors.
    """
    tests = []
    tests.append([1, 0])
    tests.append([3, 2, 1])
    tests.append([1, 3, 2, 5, 4, 6])
    tests.append([4, 1, 6, 2])
    tests.append([200, 0, 100343, 14, 7, 9, 200, 12])
    tests.append(list(reversed(range(10))))
    return tests


if __name__ == '__main__':
    funcs = []
    funcs.append(insertion_sort)
    funcs.append(selection_sort)
    funcs.append(merge_sort)
    funcs.append(heap_sort)
    funcs.append(quick_sort)
    funcs.append(hoare_quick_sort)
    funcs.append(random_quick_sort)
    funcs.append(counting_sort)
    for func in funcs:
        tests = refresh_tests()
        for test in tests:
            unit_test_sorting(func, test, 0, len(test) - 1)
        stress_test_sorting(func)
