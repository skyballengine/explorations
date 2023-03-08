# Author: Eusebius Ballentine
# GitHub username: skyballengine
# Date: 02-21-2023
# Description: Assignment 7 - Linked Lists and Recursion
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
        """
        getter for linked list's _head data member
        :return: Node
        """
        return self._head

    def rec_add(self, val, current):
        """
        Recursive method that adds a node containing val to the end of the linked
list
        :param current: parameter tracks the linked list each step of recursion
        :param val: Any
        :return: None
        """
        if self._head is None:
            self._head = Node(val)
            return
        if current.next is None:
            current.next = Node(val)
            return
        self.rec_add(val, current.next)

    def add(self, val):
        """rec_add helper method"""
        self.rec_add(val, self._head)

    def rec_remove(self, val, current):
        """
        Recursive method that removes the node containing val from the linked list
        :param current: tracks the current node through the recursion
        :param val: Any
        :return: None
        """
        if current is None:  # If the list is empty
            return
        if current.data == val:
            self._head = current.next
            return
        if current.next.data == val:
            current.next = current.next.next
            return
        self.rec_remove(val, current.next)

    def remove(self, val):
        """rec_remove helper method"""
        self.rec_remove(val, self._head)

    def rec_contains(self, val, current):
        """
        Recursive method that searches the linked list for a val and returns True
if in and False if not in
        :param current: Node
        :param val: Any
        :return: Boolean
        """
        if current.next is None and current.data != val:
            return False
        if current.data == val:
            return True
        else:
            current = current.next
            return self.rec_contains(val, current)

    def contains(self, val):
        """rec_contains helper method"""
        self.rec_contains(val, self._head)

    def rec_insert(self, val, pos, current, count):
        """
        Recursive method that inserts a Node with the argument val as it's "data"
data member
        at the position provided as pos argument
        :param count: int
        :param current: Node
        :param val: Any
        :param pos: int
        :return: None
        """
        if current is None:  # If the list is empty
            self._head = Node(val)
            return
        if pos == 0:
            temp = self._head
            self._head = Node(val)
            self._head.next = temp
            return
        count += 1
        previous = current
        current = current.next
        if pos == count:
            temp = current
            previous.next = Node(val)
            previous.next.next = temp
            return
        else:
            return self.rec_insert(val, pos, current, count)

    def insert(self, val, pos):
        """
        rec_insert helper method
        :param val: int
        :param pos: int
        :return: None
        """
        self.rec_insert(val, pos, self._head, 0)

    def rec_reverse(self, current, previous, following):
        """
        Recursively reverses the order of the Nodes in the linked list
        :return: None
        """
        if current is None:
            self._head = previous
            return
        else:
            following = current.next
            current.next = previous
            previous = current
            current = following
            return self.rec_reverse(current, previous, following)

    def reverse(self):
        """
        rec_reverse helper method
        :return: None
        """
        self.rec_reverse(self._head, None, None)

    def rec_to_plain_list(self, current, result_list):
        """
        Recursive method that returns a regular Python list containing the same
values,
        in the same order as the linked list
        :return: List
        """
        if current is None:
            return
        result_list += [current.data]
        return self.rec_to_plain_list(current.next, result_list)

    def to_plain_list(self):
        """rec_to_plain_list helper method"""
        self.rec_to_plain_list(self._head, [])

    def rec_display(self, a_node):
        """recursive display method"""
        if a_node is None:
            return
        print(a_node.data, end=" ")
        self.rec_display(a_node.next)

    def display(self):
        """rec_display helper method"""
        self.rec_display(self._head)


def main():
    linked_list1 = LinkedList()
    # test rec_add
    for i in range(1, 11):
        linked_list1.add(i)
    # test rec_remove
    linked_list1.remove(2)
    linked_list1.display()
    print()
    linked_list1.remove(1)
    linked_list1.display()
    print()
    # test rec_contains
    print(linked_list1.contains(2))
    # test rec_to_plain_list
    print(linked_list1.to_plain_list())
    # test rec_reverse
    print(linked_list1.reverse())
    linked_list1.display()
    print()
    # test rec_insert
    linked_list1.insert(111, 5)
    linked_list1.display()


if __name__ == "__main__":
    main()
