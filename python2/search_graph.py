"""
Breadth and depth first search algorithms.
"""

import sys
from copy import deepcopy
from collections import deque
from struct_graph import Vertex, Graph


def bfs(G, s):
    assert type(G) == Graph
    assert type(s) == Vertex
    for u in G.V - {s}:
        u.color = 'white'
        u.d = 10000000
        u.p = None
    s.color = 'gray'
    s.d = 0
    s.p = None
    Q = deque([s])
    while len(Q) != 0:
        u = Q.popleft()
        for v in G.Adj[u]:
            if v.color == 'white':
                v.color = 'gray'
                v.d = u.d + 1
                v.p = u
                Q.append(v)
        u.color = 'black'


def dfs(G, s):
    assert type(G) == Graph
    assert type(s) == Vertex
    for u in G.V - {s}:
        u.color = 'white'
        u.d = 10000000
        u.p = None
    s.color = 'gray'
    s.d = 0
    s.p = None
    Q = [s]
    while len(Q) != 0:
        u = Q.pop()
        for v in G.Adj[u]:
            if v.color == 'white':
                v.color = 'gray'
                v.d = u.d + 1
                v.p = u
                Q.append(v)
        u.color = 'black'


def dfs_visit(G, u, time):
    time = time + 1
    u.d = time
    u.color = 'gray'
    for v in G.Adj[u]:
        if v.color == 'white':
            v.p = u
            time = dfs_visit(G, v, time)
    u.color = 'black'
    time = time + 1
    u.f = time
    return time


def dfs_recursive(G):
    assert type(G) == Graph
    for u in G.V:
        u.color = 'white'
        u.p = None
    time = 0
    for u in G.V:
        if u.color == 'white':
            dfs_visit(G, u, time)


if __name__ == '__main__':
    G1 = Graph({'r': ['v', 's'], 'v': ['r'], 's': ['r', 'w'],
                'w': ['s', 't', 'x'], 't': ['w', 'x', 'u'],
                'x': ['w', 't', 'u', 'y'], 'y': ['u', 'x'],
                'u': ['t', 'x', 'y']})
    G2 = deepcopy(G1)
    G3 = deepcopy(G1)

    if len(sys.argv) == 2:
        if sys.argv[1] == '0':
            bfs(G1, G1.get_vertex('s'))
            for v in sorted(G1.V, key=lambda x: x.d):
                print '------------'
                print v.name
                print v.color
                print 'Shortest Path = ' + str(v.d)
                if v.p is not None:
                    print 'Parent = ' + v.p.name
                else:
                    print 'No Parent'

        elif sys.argv[1] == '1':
            dfs_recursive(G2)
            for v in sorted(G2.V, key=lambda x: x.d):
                print '------------'
                print v.name
                print v.color
                print 'Start Time = ' + str(v.d)
                print 'Finish Time = ' + str(v.f)
                if v.p is not None:
                    print 'Parent = ' + v.p.name
                else:
                    print 'No Parent'
        elif sys.argv[1] == '2':
            dfs(G3, G3.get_vertex('s'))
            for v in sorted(G3.V, key=lambda x: x.d):
                print '------------'
                print v.name
                print v.color
                print 'Shortest Path = ' + str(v.d)
                if v.p is not None:
                    print 'Parent = ' + v.p.name
                else:
                    print 'No Parent'
        else:
            print('Enter 0, 1, or 2 as input to specify an algorithm')
    else:
        print('Enter 0, 1, or 2 as input to specify an algorithm')
