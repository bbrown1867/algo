"""
Activity selection problem.
"""


def recursive_activity_selection(s, f, k, n):
    m = k + 1
    while m <= n and s[m] < f[k]:
        m = m + 1
    if m <= n:
        return set([m]) | recursive_activity_selection(s, f, m, n)
    else:
        return set()


def iterative_activty_selection(s, f, n):
    A = set([1])
    k = 1
    for m in range(2, n + 1):
        if s[m] >= f[k]:
            A = A | set([m])
            k = m
    return A


if __name__ == '__main__':
    # The first entry is the dummy entry, allowing [1:n] style indexing
    s = [0, 1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
    f = [0, 4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16]
    assert len(s) == len(f)

    result = recursive_activity_selection(s, f, 0, len(s) - 1)
    assert result == set([1, 4, 8, 11])

    result = iterative_activty_selection(s, f, len(s) - 1)
    assert result == set([1, 4, 8, 11])
