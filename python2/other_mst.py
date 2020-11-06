"""
Minimum spanning tree algorithm.
"""

from struct_graph import Graph

sets = []


def make_set(vertex):
    sets.append(set([vertex]))


def get_sets():
    return sets


def find_set(vertex):
    for s in get_sets():
        if vertex in s:
            return s
    assert False


def union(vertex_a, vertex_b):
    set_a = find_set(vertex_a)
    set_b = find_set(vertex_b)
    new_set = set_a | set_b
    del sets[sets.index(set_a)]
    del sets[sets.index(set_b)]
    sets.append(new_set)


def mst_kruskal(G, w):
    """
    Only uses the Graph object to extract vertex names, otherwise just
    operates with strings.
    """
    A = set()
    for v in G.V:
        make_set(v.name)
    for (u, v) in sorted(w, key=w.get):
        if find_set(u) != find_set(v):
            A = A | set([(u, v)])
            union(u, v)
    return A


def mst_prim(G, w, r):
    """
    Uses the Graph object to add extra fields, like search_graph.py.
    """
    for v in G.V:
        v.key = 100000
        v.p = None
    r.key = 0
    Q = [v for v in G.V]
    while len(Q) != 0:
        # Extract minimum
        u = min(Q, key=lambda x: x.key)
        del Q[Q.index(u)]
        for v in G.Adj[u]:
            try:
                weight = w[(u.name, v.name)]
            except KeyError:
                weight = w[(v.name, u.name)]
            if v in Q and weight < v.key:
                v.p = u
                v.key = weight


def tuple_compare(tuple1, tuple2):
    (u, v) = tuple1
    (u_1, v_1) = tuple2
    return (u == u_1 and v == v_1) or (v == u_1 and u == v_1)


def compare_edges(given_set, given_list):
    given_set_as_list = list(given_set)
    assert len(given_set_as_list) == len(given_list)
    for (u, v) in given_set_as_list:
        for (u_1, v_1) in given_list:
            if tuple_compare((u, v), (u_1, v_1)):
                break
        else:
            print '(%s,%s) in actual, not in expected.' % (u, v)
    for (u, v) in given_list:
        for (u_1, v_1) in given_set_as_list:
            if tuple_compare((u, v), (u_1, v_1)):
                break
        else:
            print '(%s,%s) in expected, not in actual.' % (u, v)


if __name__ == '__main__':
    G = Graph({'a': ['b', 'h'],
               'b': ['a', 'h', 'c'],
               'c': ['b', 'i', 'f', 'd'],
               'd': ['c', 'f', 'e'],
               'e': ['f', 'd'],
               'f': ['e', 'd', 'c', 'g'],
               'g': ['i', 'h', 'f'],
               'h': ['a', 'b', 'g', 'i'],
               'i': ['c', 'h', 'g']})

    w = {('a', 'b'): 4, ('b', 'c'): 8, ('c', 'd'): 7, ('d', 'e'): 9,
         ('e', 'f'): 10, ('f', 'd'): 14, ('c', 'f'): 4, ('f', 'g'): 2,
         ('g', 'i'): 6, ('g', 'h'): 1, ('i', 'h'): 7, ('h', 'a'): 8,
         ('i', 'c'): 2, ('h', 'b'): 11}

    # Make sure the graph and the weights are mapped
    for (u, v) in G.E:
        for (u_1, v_1) in w:
            # Undirected graph, so order doesn't matter
            if tuple_compare((u.name, v.name), (u_1, v_1)):
                break
        else:
            raise AssertionError('Could not find the graph edge in w')

    print 'Testing Kruskal...'
    A = mst_kruskal(G, w)
    exp = [('a', 'b'), ('a', 'h'), ('h', 'g'), ('g', 'f'),
           ('f', 'c'), ('c', 'i'), ('c', 'd'), ('d', 'e')]
    compare_edges(A, exp)
    print 'Test Complete.\r\n'

    print 'Testing Prim...'
    mst_prim(G, w, G.get_vertex('a'))
    for v in sorted(G.V, key=lambda x: x.name):
        print '------------'
        print v.name
        print 'Key = ' + str(v.key)
        if v.p is not None:
            print 'Parent = ' + v.p.name
        else:
            print 'No Parent'
    print 'Test Complete.\r\n'
