"""
Path finding algorithms for graphs.
"""

from struct_graph import Graph


def init_single_source(G, s):
    for v in G.V:
        v.d = 1000000
        v.p = None
    s.d = 0


def relax(u, v, w):
    if v.d > u.d + w[(u.name, v.name)]:
        v.d = u.d + w[(u.name, v.name)]
        v.p = u


def bellman_ford(G, w, s):
    init_single_source(G, s)
    for i in range(len(G.V) - 1):
        for (u, v) in G.E:
            relax(u, v, w)
    for (u, v) in G.E:
        if v.d > u.d + w[(u.name, v.name)]:
            return False
    return True


def min_prio_init(G):
    return [v for v in G.V]


def min_prio_get(Q):
    u = min(Q, key=lambda x: x.d)
    del Q[Q.index(u)]
    return u


def dijkstra(G, w, s):
    init_single_source(G, s)
    S = set()
    Q = min_prio_init(G)
    while len(Q) != 0:
        u = min_prio_get(Q)
        S = S | set([u])
        for v in G.Adj[u]:
            relax(u, v, w)


if __name__ == '__main__':
    # Create the graph
    G = Graph({'a': ['b'], 'b': ['c', 'd'], 'c': [], 'd': ['c']})
    w = {('a', 'b'): 4, ('b', 'd'): 1, ('b', 'c'): 3, ('d', 'c'): 5}

    # Test that no user errors while entering the graph data
    for (u, v) in G.E:
        for (x, y) in w:
            if u.name == x and v.name == y:
                break
        else:
            raise AssertionError('Could not find the graph edge in w')

    # Test bellman_ford on a non-cycle graph
    assert bellman_ford(G, w, G.get_vertex('a'))
    for v in sorted(G.V, key=lambda x: x.d):
        print '---' + v.name + '---'
        print 'Distance: ' + str(v.d)
        if v.p is not None:
            print 'Parent : ' + v.p.name
        else:
            print 'Parent : NIL'
    print 'Passed Bellman-Ford non-cycle'

    # Create the graph
    G = Graph({'a': ['b'], 'b': ['c', 'd'], 'c': [], 'd': ['c', 'b']})
    w = {('a', 'b'): 4, ('b', 'd'): 1, ('b', 'c'): 3, ('d', 'c'): 5,
         ('d', 'b'): -2}

    # Test that no user errors while entering the graph data
    for (u, v) in G.E:
        for (x, y) in w:
            if u.name == x and v.name == y:
                break
        else:
            raise AssertionError('Could not find the graph edge in w')

    # Test bellman_ford on a cycle graph
    assert not bellman_ford(G, w, G.get_vertex('a'))
    print 'Passed Bellman-Ford cycle'

    # Create the graph
    G = Graph({'a': ['b'], 'b': ['c', 'd'], 'c': [], 'd': ['c']})
    w = {('a', 'b'): 4, ('b', 'd'): 1, ('b', 'c'): 3, ('d', 'c'): 5}

    # Test dijkstra on non-cycle, same as before
    dijkstra(G, w, G.get_vertex('a'))
    for v in sorted(G.V, key=lambda x: x.d):
        print '---' + v.name + '---'
        print 'Distance: ' + str(v.d)
        if v.p is not None:
            print 'Parent : ' + v.p.name
        else:
            print 'Parent : NIL'
    print 'Passed Dijkstra non-cycle'
