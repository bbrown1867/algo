"""
Fibonacci sequence.
"""

import time


def fib(i):
    if i == 0:
        return 0
    elif i == 1:
        return 1
    else:
        return fib(i - 1) + fib(i - 2)


def fib_dynamic_helper(i, cache):
    if cache[i] is not None:
        return cache[i]
    else:
        n = fib_dynamic_helper(i - 1, cache) + fib_dynamic_helper(i - 2, cache)
        cache[i] = n
        return n


def fib_dynamic(i):
    cache = [0, 1] + [None for j in range(i-1)]
    return fib_dynamic_helper(i, cache)


def fib_dynamic_bottom_up(i):
    if i == 0:
        return 0
    elif i == 1:
        return 1
    else:
        a, b = 0, 1
        for j in range(i):
            a, b = b, a + b
        return a


if __name__ == '__main__':
    # Unit testing
    fib_answers = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
    for i in range(len(fib_answers)):
        assert fib(i) == fib_answers[i]
        assert fib_dynamic(i) == fib_answers[i]
        assert fib_dynamic_bottom_up(i) == fib_answers[i]

    # Stress testing
    time1 = time.time()
    fib(30)
    time2 = time.time()
    worse = (time2 - time1) * 1000.0
    print 'Normal Fib = %f ms' % (worse)

    time1 = time.time()
    fib_dynamic(30)
    time2 = time.time()
    best = (time2 - time1) * 1000.0
    print 'Cached Fib = %f ms' % (best)

    time1 = time.time()
    fib_dynamic_bottom_up(30)
    time2 = time.time()
    maybe = (time2 - time1) * 1000.0
    print 'Bottom-Up Fib = %f ms' % (maybe)
