"""
Maximum subarray problem.
"""


def max_crossing(A, low, mid, high):
    left_sum = -100000000
    value = 0
    i = mid
    while i >= low:
        value = value + A[i]
        if value > left_sum:
            left_sum = value
            max_left = i
        i = i - 1

    right_sum = -100000000
    value = 0
    i = mid + 1
    while i <= high:
        value = value + A[i]
        if value > right_sum:
            right_sum = value
            max_right = i
        i = i + 1

    return (max_left, max_right, left_sum + right_sum)


def max_subarray(A, low, high):
    if low == high:
        return (low, high, A[low])
    else:
        mid = (low + high) / 2
        (left_low, left_high, left_sum) = max_subarray(A, low, mid)
        (right_low, right_high, right_sum) = max_subarray(A, mid + 1, high)
        (cross_low, cross_high, cross_sum) = max_crossing(A, low, mid, high)
        if (left_sum > right_sum) and (left_sum > cross_sum):
            return (left_low, left_high, left_sum)
        elif (right_sum > left_sum) and (right_sum > cross_sum):
            return (right_low, right_high, right_sum)
        else:
            return (cross_low, cross_high, cross_sum)


def max_subarray_brute(A, low, high):
    ssum = 0
    mmax = -100000000
    left = low
    right = low
    for i in range(low, high):
        ssum = A[i]
        if ssum > mmax:
            mmax = ssum
            left = i
            right = i

        for j in range(i+1, high+1):
            ssum = ssum + A[j]
            if ssum > mmax:
                mmax = ssum
                left = i
                right = j

    return (left, right, mmax)


if __name__ == '__main__':
    A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    (low, high, value) = max_subarray(A, 0, len(A) - 1)
    print "Expected: A[7:10] = 43"
    print "Actual: A[%d:%d] = %d" % (low, high, value)

    A = [-7, 20, -7, 20]
    (low, high, value) = max_subarray(A, 0, len(A) - 1)
    print "Expected: A[1:3] = 33"
    print "Actual: A[%d:%d] = %d" % (low, high, value)

    print "-------------------- BRUTE FORCE ----------------------"

    A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    (low, high, value) = max_subarray_brute(A, 0, len(A) - 1)
    print "Expected: A[7:10] = 43"
    print "Actual: A[%d:%d] = %d" % (low, high, value)

    A = [-7, 20, -7, 20]
    (low, high, value) = max_subarray_brute(A, 0, len(A) - 1)
    print "Expected: A[1:3] = 33"
    print "Actual: A[%d:%d] = %d" % (low, high, value)
