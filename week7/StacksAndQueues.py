class Stack:
    """
    An implementation of the Stack ADT that uses Python's built-in lists
    """

    def __init__(self):
        self.list = []

    def push(self, data):
        self.list.append(data)

    def pop(self):
        val = self.list[-1]
        del self.list[-1]
        return val

    def peek(self):
        return self.list[-1]

    def is_empty(self):
        return len(self.list) == 0


class Queue:
    """
    An implementation of the Queue ADT that uses Python's built-in lists
    """

    def __init__(self):
        self.list = []

    def enqueue(self, data):
        self.list.append(data)

    def dequeue(self):
        val = self.list[0]
        del self.list[0]
        return val

    def is_empty(self):
        return len(self.list) == 0
    