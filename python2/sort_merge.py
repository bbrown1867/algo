"""
Merge sort.
"""


def merge(sub_a, sub_b):
    true_len = len(sub_a + sub_b)
    sub_a.append(max(sub_b)+1)
    sub_b.append(max(sub_a)+1)
    new_ls = []
    a = b = 0
    for i in range(true_len):
        if sub_a[a] < sub_b[b]:
            new_ls.append(sub_a[a])
            a = a + 1
        else:
            new_ls.append(sub_b[b])
            b = b + 1
    return new_ls


def merge_sort(ls, start, end):
    if (start < end):
        middle = (start + end) / 2
        sub_a = merge_sort(ls, start, middle)
        sub_b = merge_sort(ls, middle + 1, end)
        result = merge(sub_a, sub_b)
    else:
        result = [ls[start]]
    return result
