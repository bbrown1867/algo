"""
Linked list.
"""

from sort_insertion import insertion_sort


class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def __str__(self):
        if self.data is not None:
            return str(self.data)
        else:
            return 'Empty Node'


class LinkedList(object):

    def __init__(self, head=None):
        self.head = head

    def __str__(self):
        if self.head is not None:
            st = 'Head: ' + str(self.head) + ' --> '
            curr_node = self.head.next_node
            while curr_node is not None:
                st += 'Node: ' + str(curr_node.data) + ' --> '
                curr_node = curr_node.next_node
            st += 'NULL'
        else:
            st = 'Empty LinkedList'
        return st

    def insert(self, data):
        new_node = Node(data, self.head)
        self.head = new_node

    def search(self, data):
        curr_node = self.head
        while curr_node is not None:
            if curr_node.data == data:
                break
            curr_node = curr_node.next_node
        return curr_node

    def delete(self, data):
        if data == self.head.data:
            self.head = self.head.next_node
        else:
            prev_node = self.head
            curr_node = self.head.next_node
            while curr_node is not None:
                if curr_node.data == data:
                    prev_node.next_node = curr_node.next_node
                    break
                prev_node = curr_node
                curr_node = curr_node.next_node

    def reset(self):
        self.head = None

    def convert_to_list(self):
        ls = []
        curr_node = self.head
        while curr_node is not None:
            ls.append(curr_node.data)
            curr_node = curr_node.next_node
        return ls

    def sort(self):
        ls = self.convert_to_list()
        self.reset()
        insertion_sort(ls)
        for val in reversed(ls):
            self.insert(val)
