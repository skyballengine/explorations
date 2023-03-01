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
        current = self._head
        while current is not None:
            print(current, end=" ")
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
        count = 0
        if self._head is None:  # If the list is empty
            self._head = Node(val)
            return

        if pos == 0:
            temp = self._head
            self._head = Node(val)
            self._head.next = temp
            return

        current = self._head
        while current.next is not None:
            count += 1
            previous = current
            current = current.next
            if pos == count:
                temp = current
                previous.next = Node(val)
                previous.next.next = temp
                return

        current.next = Node(val)

    def reverse(self):
        """"
        Reverses the linked list
        """
        # list_version = self.to_regular_list()
        previous = None
        current = self._head

        while current is not None:
            # list_version = self.to_regular_list()
            # print(list_version)
            following = current.next
            current.next = previous
            previous = current
            current = following
        self._head = previous

    def rec_display(self, a_node):
        """recursive display method"""
        if a_node is None:
            return

        print(a_node.data, end=" ")
        self.rec_display(a_node.next)

    def display_r(self):
        """recursive display helper method"""
        self.rec_display(self._head)

        # memo_dict = {}
        # count = 0
        # current = self._head
        # while current is not None:
        #     memo_dict[count] = current
        #     previous = current
        #     current = current.next
        #     count += 1
        #
        # memo_keys_list = list(reversed(list(memo_dict.keys())))
        # print(memo_keys_list)
        # for key in memo_keys_list:
        #     if key == 0:
        #         self._head = memo_dict[key]
        #     else:
        #         self.add(memo_dict[key])


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
    print(linked_list.to_regular_list())

    # reverse method
    linked_list.reverse()
    linked_list.display()
    print(linked_list.to_regular_list())

    # exercise 2 - insert method
    # print(linked_list.to_regular_list())
    # linked_list.insert(2, 0)
    # # linked_list.insert(2, 2)
    # print(linked_list.to_regular_list())
    # linked_list.insert(13, 8)
    # print(linked_list.to_regular_list())
    # linked_list.insert(13, 2)
    # print(linked_list.to_regular_list())
    # linked_list.insert(14, 5)
    # print(linked_list.to_regular_list())


if __name__ == "__main__":
    main()
