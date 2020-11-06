"""
Priority queue implementation using a heap.
"""

from struct_heap import Heap


class PriorityQueue(Heap):

    def __init__(self, ls):
        super(PriorityQueue, self).__init__(ls)
        self.max_heap_build()

    def peek(self):
        return self[0]

    def extract(self):
        if self.heap_size < 1:
            raise Exception('Heap underflow')
        m = self[0]
        self[0] = self[-1]
        del self[-1]
        self.heap_size = self.heap_size - 1
        self.max_heapify()
        return m


if __name__ == '__main__':
    A = PriorityQueue([10, 22, 35, 1, 14, 2, 200, 500, 100])

    # Testing get_max
    m = A.peek()
    assert m == 500

    # Testing extract max
    m = A.extract()
    assert m == 500
    assert not (500 in A)
