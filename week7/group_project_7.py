# Author: Michael Galvan Jr.
# GitHub Username: mickey-2k
# Date: 02/22/2023
# Description: Creates a Linked List that uses recursive methods to add, remove,
# reverse, insert, print a list
#              and see if a value is contained within the list.
class Node:
    """
    Represents a node in a linked list
    """

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """
    A linked list implementation of the List ADT
    """

    def __init__(self):
        self._head = None

    def get_head(self):
        """Returns the first Node object in the list"""
        return self._head

    def add(self, value):
        """
        Adds a node containing val to the end of the linked list
        """
        if self._head is None:
            self._head = Node(value)
            return
        self.rec_add(value, self._head)

    def rec_add(self, value, a_node):
        """recursive add helper method"""
        if a_node.next is None:
            a_node.next = Node(value)
            return
        self.rec_add(value, a_node.next)

    def remove(self, value):
        """Removes the node containing the value from the linked list"""
        if self._head is None:
            return
        if self._head.data == value:
            self._head = self._head.next
            return
        self.rec_remove(value, self._head, self._head)

    def rec_remove(self, value, a_node, prev_node):
        """recursive remove helper method"""
        if a_node.data == value:
            prev_node.next = a_node.next
            return
        self.rec_remove(value, a_node.next, a_node)

    def contains(self, value):
        """Looks for a value in the linked list and returns True if it is in the
list and False otherwise"""
        if self._head is None:
            return False
        return self.rec_contains(value, self._head)

    def rec_contains(self, value, a_node):
        """recursive contains helper method"""
        if a_node.data == value:
            return True
        if a_node.data != value and a_node.next is not None:
            a_node = a_node.next
            return self.rec_contains(value, a_node)
        else:
            return False

    def insert(self, value, position):
        """Inserts a value into the given position in the linked list"""
        if self._head is None and position >= 0:
            self._head = Node(value)
            return
        if self._head is not None and position == 0:
            b_node = self._head
            self._head = Node(value)
            self._head.next = b_node
            return
        self.rec_insert(value, position, self._head, self._head)

    def rec_insert(self, value, position, a_node, prev_node):
        """recursive insert helper method"""
        if position >= 1 and a_node.next is None:
            a_node.next = Node(value)
            return
        elif a_node.next is not None and position > 0:
            position -= 1
            prev_node = a_node
            self.rec_insert(value, position, a_node.next, prev_node)
            return
        elif position == 0:
            prev_node.next = Node(value)
            b_node = prev_node.next
            b_node.next = a_node
            return

    def reverse(self):
        """Reverses the order of the linked list"""
        if self._head is None:
            return
        if self._head.next is None:
            return
        self.rec_reverse(self._head, None, None)

    def rec_reverse(self, a_node, b_node, prev_node):
        """recursive reverse helper method"""
        b_node = a_node.next
        a_node.next = prev_node
        prev_node = a_node
        a_node = b_node
        if a_node is None:
            self._head = prev_node
            return
        self.rec_reverse(a_node, b_node, prev_node)

    def to_plain_list(self):
        """Returns a regular Python list that has the same values, in the same
order as the current
        state of the linked list"""
        if self._head is None:
            return []
        self.rec_to_plain_list(self._head, [])

    def rec_to_plain_list(self, a_node, l_list):
        """recursive to_plain_list helper method"""
        if a_node is not None:
            b_node = a_node.next
            l_list.append(a_node.data)
            a_node = b_node
            if a_node is None:
                l_list = l_list
                return l_list
            self.rec_to_plain_list(a_node, l_list)
            a_node.data

    def rec_display(self, a_node):
        """recursive display method"""
        if a_node is None:
            return
        print(a_node.data, end=" ")
        self.rec_display(a_node.next)

    def display(self):
        """rec_display helper method"""
        self.rec_display(self._head)


test_ll = LinkedList()
print(test_ll.contains(21))
test_ll.add(21)
test_ll.add(22)
test_ll.add(23)
test_ll.add(24)
print(test_ll.contains(21))
test_ll.remove(23)
test_ll.remove(21)
print(test_ll.contains(23))
print(test_ll.contains(21))
print(test_ll.contains(22))
test_ll.insert(25, 2)
test_ll.insert(78, 0)
test_ll.insert(33, 8)
test_ll.insert(23, 2)
print(test_ll.display())
test_ll.reverse()
print(test_ll.display())
print(test_ll.to_plain_list())
print('Hi')
