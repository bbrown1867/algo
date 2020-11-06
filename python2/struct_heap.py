"""
Heap.
"""


def parent(i):
    if i > 0:
        return (i - 1) / 2
    else:
        return i


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def is_min_heapify(A):
    return all([A[parent(i)] <= A[i] for i in range(1, A.heap_size)])


def is_max_heapify(A):
    return all([A[parent(i)] >= A[i] for i in range(1, A.heap_size)])


class Heap(list):

    def __init__(self, ls):
        super(Heap, self).__init__(ls)
        self.heap_size = len(ls)

    def __str__(self):
        if self.heap_size < 15:
            vals = self.heap_size
            append = ']'
        else:
            vals = 15
            append = '... ]'
        string = '['
        for v in self[:vals]:
            string += str(v) + ', '
        string += append
        return string

    def min_heapify(self, i=0):
        lf = left(i)
        rt = right(i)
        smallest = i

        if lf < self.heap_size and self[lf] < self[i]:
            smallest = lf

        if rt < self.heap_size and self[rt] < self[smallest]:
            smallest = rt

        if smallest != i:
            self[i], self[smallest] = self[smallest], self[i]
            self.min_heapify(smallest)

    def max_heapify(self, i=0):
        lf = left(i)
        rt = right(i)
        largest = i

        if lf < self.heap_size and self[lf] > self[i]:
            largest = lf

        if rt < self.heap_size and self[rt] > self[largest]:
            largest = rt

        if largest != i:
            self[i], self[largest] = self[largest], self[i]
            self.max_heapify(largest)

    def max_heap_build(self):
        for i in reversed(range(self.heap_size / 2)):
            self.max_heapify(i)

    def max_heap_delete(self, i):
        if i == self.heap_size - 1:
            del self[-1]
            self.heap_size = self.heap_size - 1
            return
        else:
            self[i] = self[-1]
            del self[-1]
            self.heap_size = self.heap_size - 1

        going_up = False
        while i > 0 and self[parent(i)] < self[i]:
            going_up = True
            self[parent(i)], self[i] = self[i], self[parent(i)]
            i = parent(i)

        if not going_up:
            self.max_heapify(i)

    def max_heap_insert(self, key):
        self.heap_size = self.heap_size - 1
        self.append(key - 1)
        self.max_heap_increase_key(self.heap_size - 1, key)

    def max_heap_increase_key(self, i, key):
        if key < self[i]:
            raise Exception('New key smaller than current key')
        else:
            self[i] = key
            while i > 0 and A[parent(i)] < A[i]:
                self[parent(i)], self[i] = self[i], self[parent(i)]
                i = parent(i)


if __name__ == '__main__':
    # Testing min heapify
    A = Heap([1, 12, 3, 4, 5, 6, 7, 6, 7])
    assert not is_min_heapify(A)
    A.min_heapify(1)
    assert is_min_heapify(A)

    # Testing max_heapify
    A = Heap([16, 4, 10, 14, 7, 9, 3, 2, 8, 1])
    assert not is_max_heapify(A)
    A.max_heapify(1)
    assert is_max_heapify(A)

    # Testing delete
    init = A.heap_size
    A.max_heap_delete(0)
    assert is_max_heapify(A)
    assert A.heap_size == (init - 1)

    # Testing increase key
    last = A.heap_size - 1
    orig = A[last]
    A.max_heap_increase_key(last, orig + 20)
    assert not (orig in A)
    assert (orig + 20 in A)
    assert is_max_heapify(A)

    # Testing insert
    A.max_heap_insert(50)
    assert (50 in A)
    assert is_max_heapify(A)
