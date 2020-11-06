"""
Hash table.
"""

import math
from struct_linkedlist import LinkedList, Node


class HashTableChained(object):

    def __init__(self, size=0, func=None):
        self.T = [LinkedList() for i in range(size)]
        self.size = size
        self.func = func

    def h(self, k):
        if self.func == 'direct':
            return k
        elif self.func == 'div':
            return k % self.size
        elif self.func == 'mult':
            knuth = (math.sqrt(5.0) - 1.0) / 2.0
            return int((math.floor(self.size * ((k*knuth) % 1.0))))
        else:
            raise Exception('Error: Hash function not supported.')

    def insert(self, k):
        self.T[self.h(k)].insert(k)

    def search(self, k):
        return self.T[self.h(k)].search(k)

    def delete(self, k):
        self.T[self.h(k)].delete(k)

    def __str__(self):
        st = '----T----\r\n'
        for t in self.T:
            st += str(t) + '\r\n'
        return st


class HashTableOpenAddressing(HashTableChained):

    def __init__(self, size=0, func=None, probe_func=None):
        self.T = [None for i in range(size)]
        self.size = size
        self.func = func
        self.probe_func = probe_func

    def aux_h(self, k):
        return 1 + (k % self.size)

    def probe(self, k, i):
        if self.probe_func == 'linear':
            return (self.h(k) + i) % self.size
        elif self.probe_func == 'double':
            return (self.h(k) + i*self.aux_h(k)) % self.size
        else:
            raise Exception('Error: Probe function not supported.')

    def insert(self, k):
        i = 0
        while i < self.size:
            j = self.probe(k, i)
            if self.T[j] is None or self.T[j] == 'DELETED':
                self.T[j] = k
                return
            else:
                i = i + 1
        raise Exception('Error: Overflow')

    def search(self, k):
        i = 0
        while i < self.size:
            j = self.probe(k, i)
            if self.T[j] == k:
                return self.T[j]
            elif self.T[j] is None:
                break
            else:
                i = i + 1
        return None

    def search_for_index(self, k):
        i = 0
        while i < self.size:
            j = self.probe(k, i)
            if self.T[j] == k:
                return j
            elif self.T[j] is None:
                break
            else:
                i = i + 1
        return None

    def delete(self, k):
        j = self.search_for_index(k)
        if j is None:
            return
        else:
            self.T[j] = 'DELETED'


def unit_testing(h):
    # Test insertion
    h.insert(4)
    h.insert(10)
    h.insert(0)
    h.insert(1)
    try:
        h.insert(101)
        h.insert(200)
        h.insert(200)
        h.insert(200)
    except IndexError:
        print 'Hash fn does not support values larger than table size\r\n'
    print h

    # Test deletion
    h.delete(10)
    node = h.search(10)
    assert node is None
    try:
        h.delete(101)
        node = h.search(101)
        assert node is None
    except IndexError:
        print 'Hash fn does not support values larger than table size\r\n'
    print h

    # Test searching
    node = h.search(1)
    print 'Search for 1 yielded %s\r\n' % (str(node))


if __name__ == '__main__':
    print 'Chained Testing'
    unit_testing(HashTableChained(11, 'direct'))
    unit_testing(HashTableChained(11, 'div'))
    unit_testing(HashTableChained(11, 'mult'))

    print 'Open Addressing Testing'
    unit_testing(HashTableOpenAddressing(11, 'div', 'linear'))
    unit_testing(HashTableOpenAddressing(11, 'div', 'double'))
