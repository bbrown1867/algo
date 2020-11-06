"""
Rodcutting.
"""


def cut_rod_top_down(p, n):
    """
    Only difference from book is i + 1 in recursion since the loop bounds are
    different to allow direct lookup of p[i] which is indexed different.
    """
    if n == 0:
        return 0
    else:
        q = -100000
        for i in range(n):
            q = max(q, p[i] + cut_rod_top_down(p, n - (i + 1)))
        return q


def cut_rod_top_down_cache_helper(p, n, r):
    """
    Only difference from book is i + 1 in recursion since the loop bounds are
    different to allow direct lookup of p[i] which is indexed different.
    """
    if r[n] >= 0:
        return r[n]
    if n == 0:
        return 0
    else:
        q = -100000
        for i in range(n):
            q = max(q, p[i] + cut_rod_top_down_cache_helper(p, n - (i + 1), r))
        r[n] = q
        return q


def cut_rod_top_down_cache(p, n):
    """
    Only difference from book is creating the array to n+1 since range doesn't
    include the end bound.
    """
    r = [-100000 for i in range(n + 1)]
    return cut_rod_top_down_cache_helper(p, n, r)


def cut_rod_bottom_up(p, n):
    """
    Only difference from book is p[i-1] instead of p[i] due to indexing, also
    create to arrays to n+1 since range doesn't include end bound.
    """
    r = [0 for k in range(n+1)]
    for j in range(1, n+1):
        q = -100000
        for i in range(1, j+1):
            q = max(q, p[i-1] + r[j-i])
        r[j] = q
    return r[n]


def cut_rod_bottom_up_extended(p, n):
    """
    Only difference from book is p[i-1] instead of p[i] due to indexing, also
    create to arrays to n+1 since range doesn't include end bound.
    """
    r = [0 for k in range(n+1)]
    s = [0 for k in range(n+1)]
    for j in range(1, n+1):
        q = -100000
        for i in range(1, j+1):
            # If making a cut, log it into s
            if q < p[i-1] + r[j-i]:
                q = p[i-1] + r[j-i]
                s[j] = i
        r[j] = q
    return r, s


def print_cut_rod_bottom_up_extended(p, n):
    (r, s) = cut_rod_bottom_up_extended(p, n)
    while n > 0:
        print s[n]
        n = n - s[n]


def cut_rod_bottom_up_cost(p, n, c):
    """
    Only difference from book is p[i-1] instead of p[i] due to indexing, also
    create to arrays to n+1 since range doesn't include end bound.
    """
    r = [0 for k in range(n+1)]
    for j in range(1, n+1):
        q = -100000
        for i in range(1, j+1):
            # There is only ever one cut per j loop, we are just changing
            # where that cut takes place. The other cuts are "embedded" in the
            # subproblems stored in r. The r[0] iteration represents no cut,
            # so otherwise there is a cut which is account for in "c".
            if i == j:
                new_q = p[i-1] + r[j-i]
            else:
                new_q = p[i-1] + r[j-i] - c
            # Now compute the max like normal
            q = max(q, new_q)
        r[j] = q
    return r[n]


if __name__ == '__main__':
    # Prices for lengths
    p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]

    # Optimal revenue for lengths
    r = [1, 5, 8, 10, 13, 17, 18, 22, 25, 30]

    # Test rod cutting
    for i in range(len(p)):
        assert cut_rod_top_down(p, i + 1) == r[i]
        assert cut_rod_top_down_cache(p, i + 1) == r[i]
        assert cut_rod_bottom_up(p, i + 1) == r[i]

    # Test extended rod cutting, which will print cut locations
    print 'Cuts for n = 10 for optimal revenue:'
    print_cut_rod_bottom_up_extended(p, 10)
    print 'Cuts for n = 7 for optimal revenue:'
    print_cut_rod_bottom_up_extended(p, 7)

    # Test the bottom cutting with cost per cut
    print 'Testing bottom up rod cutting with cost per cut...'
    # The first three are optimal with no cuts anyways, so expect the same...
    assert cut_rod_bottom_up_cost(p, 1, 1) == 1
    assert cut_rod_bottom_up_cost(p, 2, 1) == 5
    assert cut_rod_bottom_up_cost(p, 3, 1) == 8
    # The cost of the cut should reduce this from 10 to 9
    assert cut_rod_bottom_up_cost(p, 4, 1) == 9
    assert cut_rod_bottom_up_cost(p, 5, 1) == 12
    print 'Tests passed!'
