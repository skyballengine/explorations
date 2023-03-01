# Write a LinkedList method named contains, that takes a value as a parameter and returns True if that value is in
# the linked list, but returns False otherwise.

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

    def add(self, val):
        """
        Adds a node containing val to the end of the linked list
        """
        if self._head is None:  # If the list is empty
            self._head = Node(val)
        else:
            current = self._head
            while current.next is not None:
                current = current.next
            current.next = Node(val)

    def display(self):
        """
        Prints out the values in the linked list
        """
        current = self._head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()

    def remove(self, val):
        """
        Removes the node containing val from the linked list
        """
        if self._head is None:  # If the list is empty
            return

        if self._head.data == val:  # If the node to remove is the head
            self._head = self._head.next
        else:
            current = self._head
            while current is not None and current.data != val:
                previous = current
                current = current.next
            if current is not None:  # If we found the value in the list
                previous.next = current.next

    def is_empty(self):
        """
        Returns True if the linked list is empty,
        returns False otherwise
        """
        return self._head is None

    def to_regular_list(self):
        """
        Returns a regular Python list containing the same values, in the same order, as the linked list
        """
        result = []
        current = self._head
        while current is not None:
            result += [current.data]
            current = current.next
        return result

    def contains(self, val):
        if self._head is None:
            return False

        current = self._head
        while current.next is not None:
            if current.data == val:
                return True
            current = current.next
        return False

    def insert(self, val, pos):



def main():
    # exercise 1 - contains method
    linked_list = LinkedList()
    val_list = [1, 140, "hello", 1001, "why"]
    for val in val_list:
        linked_list.add(val)
    linked_list.display()
    print(linked_list.contains(1001))
    print(linked_list.contains(1))
    print(linked_list.contains(100))
    linked_list_2 = LinkedList()
    print(linked_list_2.contains(8))

    # exercise 2 - insert method



if __name__ == "__main__":
    main()
