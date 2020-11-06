"""
Optimal binary search tree.
"""


def optimal_bst(p, n):
    ls = [0.0 for i in range(n + 1)]
    e = [ls for i in range(n + 1)]
    w = [ls for i in range(n + 1)]
    ls = [0 for i in range(n)]
    root = [ls for i in range(n)]
    for level in range(n):
        for i in range(n - level):
            j = i + level
            e[i][j] = 10000.0
            w[i][j] = w[i][j - 1] + p[j]
            for r in range(i, j + 1):
                t = e[i][r - 1] + e[r + 1][j] + w[i][j]
                if t < e[i][j]:
                    e[i][j] = t
                    root[i][j] = r
    return (e, root)


if __name__ == '__main__':
    p = [0.25, 0.2, 0.05, 0.2, 0.3]
    (e, root) = optimal_bst(p, 5)

    for i in range(len(e)):
        for j in range(len(e)):
            if j >= i:
                dbg = i, j
                print 'Expected Search Cost of Opt BST for Keys %d to %d' % dbg
                print e[i][j]

    for i in range(len(root)):
        for j in range(len(root)):
            if j >= i:
                dbg = i, j
                print 'Optimal Sub-Tree Root for Keys %d --> %d' % dbg
                print root[i][j]
