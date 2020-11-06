"""
Binary search tree.
"""


class Node(object):

    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.key)


class BST(object):

    def __init__(self, root_key=None):
        if root_key is not None:
            self.root = Node(root_key)

    def walk(self, start):
        if start is not None:
            self.walk(start.left)
            if start == self.root:
                print 'ROOT: ' + str(start)
            else:
                print start
            self.walk(start.right)

    def walk_pre(self, start):
        if start is not None:
            if start == self.root:
                print 'ROOT: ' + str(start)
            else:
                print start
            self.walk(start.left)
            self.walk(start.right)

    def walk_post(self, start):
        if start is not None:
            self.walk(start.left)
            self.walk(start.right)
            if start == self.root:
                print 'ROOT: ' + str(start)
            else:
                print start

    def search(self, start, key):
        if start is None or start.key == key:
            return start
        else:
            if key < start.key:
                return self.search(start.left, key)
            else:
                return self.search(start.right, key)

    def search_iterative(self, start, key):
        while start is not None and start.key != key:
            if key < start.key:
                start = start.left
            else:
                start = start.right
        return start

    def min(self, start):
        while start.left is not None:
            start = start.left
        return start

    def max(self, start):
        while start.right is not None:
            start = start.right
        return start

    def insert(self, key):
        z = Node(key)
        y = None
        x = self.root
        # Find the home for the node satisfying BST property
        while x is not None:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        # Insert the node
        z.parent = y
        if y is None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

    def transplant(self, u, v):
        """
        Helper function for 'delete'. Replaces 'u' with subtree at 'v'.
        """
        if u.parent is None:
            # In case u is the root
            self.root = v
        elif u == u.parent.left:
            # Setup the old tree to point to the new node
            u.parent.left = v
        else:
            # Setup the old tree to point to the new node
            u.parent.right = v

        if v is not None:
            # Setup the new node to point to the old tree
            v.parent = u.parent

    def delete(self, key):
        z = self.search(self.root, key)
        if z is None:
            print 'Case 0: Node does not exist'
            return
        else:
            if z.left is None:
                print 'Case 1: No left node'
                self.transplant(z, z.right)
            elif z.right is None:
                print 'Case 2: No right node'
                self.transplant(z, z.left)
            else:
                y = self.min(z.right)
                if y.parent != z:
                    print 'Case 4: Successor not immediate child'
                    self.transplant(y, y.right)
                    y.right.parent = y
                else:
                    print 'Case 3: Successor is immediate child'
                self.transplant(z, y)
                y.left = z.left
                y.left.parent = y


def create_test_tree():
    # Test constructor
    T = BST(15)

    # Test insertion
    T.insert(11)
    T.insert(20)
    T.insert(50)
    T.insert(1)
    T.insert(21)
    T.insert(60)
    T.insert(49)
    T.insert(19)
    T.insert(16)

    return T


if __name__ == '__main__':
    T = create_test_tree()

    # Test walking
    print '\r\n'
    T.walk_pre(T.root)
    print '\r\n'
    T.walk(T.root)
    print '\r\n'
    T.walk_post(T.root)
    print '\r\n'

    # Test searching
    res = T.search_iterative(T.root, 15)
    assert res.key == 15
    res = T.search_iterative(T.root, 21)
    assert res.key == 21
    res = T.search_iterative(T.root, 200)
    assert res is None
    res = T.search(T.root, 15)
    assert res.key == 15
    res = T.search(T.root, 21)
    assert res.key == 21
    res = T.search(T.root, 200)
    assert res is None

    # Test min and max
    res = T.min(T.root)
    assert res.key == 1
    res = T.max(T.root)
    assert res.key == 60

    # Test deletion
    T.delete(343434)
    T.delete(21)
    assert T.search(T.root, 21) is None
    T = create_test_tree()
    T.delete(19)
    assert T.search(T.root, 19) is None
    T = create_test_tree()
    T.delete(50)
    assert T.search(T.root, 50) is None
    T = create_test_tree()
    T.delete(20)
    assert T.search(T.root, 20) is None
