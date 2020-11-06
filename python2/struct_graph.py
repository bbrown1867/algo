"""
Graph.
"""


class Vertex(object):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return str(self.name)


class Graph(object):

    def __init__(self, adj):
        """
        Given a dictionary containing vertices as keys, and values as a list
        of edges, convert them to Vertex objects and store as "Adj".
        """
        lookup = {key: Vertex(key) for key in adj}
        self.Adj = {}
        for key in adj:
            self.Adj[lookup[key]] = [lookup[x] for x in adj[key]]

    @property
    def V(self):
        return set([key for key in self.Adj])

    @property
    def E(self):
        return [(v, u) for v in self.Adj for u in self.Adj[v]]

    def get_vertex(self, name):
        for v in self.V:
            if v.name == name:
                return v
        return None

    def __str__(self):
        return str(self.Adj)


if __name__ == '__main__':
    # Square graph
    adj = {'a': ['b', 'c'], 'b': ['a', 'd'],
           'c': ['a', 'd'], 'd': ['b', 'c']}

    # Build the graph
    G = Graph(adj)

    # These will print memory locations of objects
    print(G)
    print(G.V)
    print(G.E)

    # Test iterating over keys
    for v in G.V:
        print v

    # Test iterating over edges
    for (u, v) in G.E:
        print(str(u), str(v))

    # Test iterating over adjacency list
    for v in G.V:
        for u in G.Adj[v]:
            print u
