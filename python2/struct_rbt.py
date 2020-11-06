"""
Red black tree.
"""


class Node(object):

    def __init__(self, key, color, parent, left, right):
        self.key = key
        self.color = color
        self.parent = parent
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.key) + ' : ' + self.color


class RBT(object):

    def __init__(self, root_key):
        self.nil = Node(0, 'black', None, None, None)
        self.root = Node(root_key, 'black', self.nil, self.nil, self.nil)

    def insert_basic(self, key, color):
        z = Node(key, color, self.nil, self.nil, self.nil)
        y = self.nil
        x = self.root
        while x != self.nil:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y == self.nil:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

    def walk(self, start):
        if start != self.nil:
            self.walk(start.left)
            if start == self.root:
                print '(ROOT) ' + str(start)
            else:
                print start
            self.walk(start.right)

    def search(self, start, key):
        if start == self.nil or start.key == key:
            return start
        else:
            if key < start.key:
                return self.search(start.left, key)
            else:
                return self.search(start.right, key)

    def get_bh(self, ls, orig, curr, ssum):
        """
        Find the black height of 'orig' and also store all black heights into
        the list 'ls'.
        """
        if curr == self.nil:
            ls.append(ssum + 1)
            return 1

        if curr.color == 'black' and curr != orig:
            add = 1
        else:
            add = 0

        x = self.get_bh(ls, orig, curr.left, ssum + add)
        y = self.get_bh(ls, orig, curr.right, ssum + add)
        return min(x, y) + add

    def property1(self, start):
        if start != self.nil:
            self.property1(start.left)
            assert start.color == 'red' or start.color == 'black'
            self.property1(start.right)

    def property2(self):
        assert self.root.color == 'black'

    def property3(self):
        assert self.nil.color == 'black'

    def property4(self, start):
        if start != self.nil:
            self.property4(start.left)
            if start.color == 'red':
                assert start.left.color == 'black'
                assert start.right.color == 'black'
            self.property4(start.right)

    def property5(self, start):
        if start != self.nil:
            self.property5(start.left)
            ###
            ls = []
            calc_bh = self.get_bh(ls, start, start, 0)
            assert ls.count(ls[0]) == len(ls)
            try:
                # Some unit testing, check the black height...
                bh = start.bh
                assert calc_bh == bh
            except AttributeError:
                pass

            self.property5(start.right)

    def verify_properties(self):
        self.property1(self.root)
        self.property2()
        self.property3()
        self.property4(self.root)
        self.property5(self.root)

    def left_rotate(self, x):
        # Precondition
        assert x.right != self.nil

        # Set y
        y = x.right

        # Rotation step!
        x.right = y.left
        if y.left != self.nil:
            y.left.parent = x
        y.parent = x.parent

        # Link up the rest of the tree with y
        if x.parent == self.nil:
            self.root = y
        elif x.parent.left == x:
            x.parent.left = y
        else:
            x.parent.right = y

        # Link x and y together
        y.left = x
        x.parent = y
        return (y, x)

    def right_rotate(self, x):
        # Precondition
        assert x.left != self.nil

        # Set y
        y = x.left

        # Rotation step!
        x.left = y.right
        if y.right != self.nil:
            y.right.parent = x
        y.parent = x.parent

        # Link up the reset of tree with y
        if x.parent == self.nil:
            self.root = y
        elif x.parent.left == x:
            x.parent.left = y
        else:
            x.parent.right = y

        # Link x and y together
        y.right = x
        x.parent = y
        return (y, x)

    def insert(self, key):
        self.insert_basic(key, 'red')
        z = self.search(self.root, key)
        self.insert_fixup(z)

    def insert_fixup(self, z):
        while z.parent.color == 'red':
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right

                # y (z's uncle) is red
                if y.color == 'red':
                    z.parent.color = 'black'
                    y.color = 'black'
                    z.parent.parent.color = 'red'
                    z = z.parent.parent

                # y (z's uncle) is black
                else:
                    # z is a right child
                    if z == z.parent.right:
                        z = z.parent
                        self.left_rotate(z)

                    # At this point z is a left child
                    z.parent.color = 'black'
                    z.parent.parent.color = 'red'
                    self.right_rotate(z.parent.parent)
            else:
                raise Exception('TODO!')
        self.root.color = 'black'


def print_verbose(node):
    print '\r\nParent = ' + str(node.parent)
    print 'Node = ' + str(node)
    print 'L = (' + str(node.left) + ')\tR = (' + str(node.right) + ')\r\n'


if __name__ == '__main__':

    # Create a test tree
    x = RBT(19)
    x.insert_basic(10, 'black')
    x.insert_basic(35, 'red')
    x.insert_basic(22, 'black')
    x.insert_basic(53, 'black')
    x.insert_basic(29, 'red')
    x.insert_basic(61, 'red')

    x.search(x.root, 19).bh = 2
    x.search(x.root, 10).bh = 1
    x.search(x.root, 35).bh = 2
    x.search(x.root, 22).bh = 1
    x.search(x.root, 53).bh = 1
    x.search(x.root, 29).bh = 1
    x.search(x.root, 61).bh = 1

    # Print the test tree
    print 'Starting RBT Walk!'
    x.walk(x.root)
    print 'End of RBT Walk!'

    # Verify the RBT properties
    print 'Testing RBT Properties...'
    x.verify_properties()
    print 'Valid RBT!'

    # Test left rotate
    print 'Testing left rotate...'
    node = x.search(x.root, 22)
    pp = node.parent
    print_verbose(pp)
    print_verbose(node)
    node, old = x.left_rotate(node)
    print_verbose(node)
    print_verbose(pp)
    print_verbose(old)

    # Test right rotate
    print 'Testing right rotate...'
    node = x.search(x.root, 29)
    pp = node.parent
    print_verbose(pp)
    print_verbose(node)
    node, old = x.right_rotate(node)
    print_verbose(node)
    print_verbose(pp)
    print_verbose(old)

    # Test insert
    z = RBT(11)
    z.insert_basic(2, 'red')
    z.insert_basic(14, 'black')
    z.insert_basic(1, 'black')
    z.insert_basic(7, 'black')
    z.insert_basic(15, 'red')
    z.insert_basic(5, 'red')
    z.insert_basic(8, 'red')
    z.walk(z.root)
    print 'Testing insert...'
    z.insert(4)
    z.walk(z.root)
    z.verify_properties()
