#!python

from linkedlist import LinkedList, Node


# Implement LinkedQueue below, then change the assignment at the bottom
# to use this Queue implementation to verify it passes all tests
class LinkedQueue(object):

    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any."""
        # Initialize a new linked list to store the items
        self.linked_list = LinkedList()
        if iterable is not None:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue."""
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise."""
        if self.linked_list.size == 0:
            return True
        return False

    def length(self):
        """Return the number of items in this queue."""
        return self.linked_list.length()

    def enqueue(self, item):
        """Insert the given item at the back of this queue.
        Running time: O(1) – Why? You are appending at the end of the LinkList, """
        self.linked_list.append(item)

    def front(self):
        """Return the item at the front of this queue without removing it,
        or None if this queue is empty."""
        if self.linked_list.is_empty():
            return None
        return self.linked_list.head.data

    def dequeue(self):
        """Remove and return the item at the front of this queue,
        or raise ValueError if this queue is empty.
        Running time: O(???) – Why? [TODO]"""
        if self.is_empty():
            raise ValueError("No items in Queue to Dequeue")
        item = self.linked_list.head.data
        self.linked_list.delete(item)
        return item


# Implement ArrayQueue below, then change the assignment at the bottom
# to use this Queue implementation to verify it passes all tests
class ArrayQueue(object):

    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any."""
        # Initialize a new list (dynamic array) to store the items
        self.python3_dynamic_array = list()
        if iterable is not None:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue."""
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise."""
        if len(self.python3_dynamic_array) == 0:
            return True
        return False

    def length(self):
        """Return the number of items in this queue."""
        return len(self.python3_dynamic_array)

    def enqueue(self, item):
        """Insert the given item at the back of this queue.
        Running time: O(1) – Why? The python3 dynamic array when placing something
        at the end doesnt need to move any index it just makes the space in memory
        have one more place next to it."""
        return self.python3_dynamic_array.append(item)

    def front(self):
        """Return the item at the front of this queue without removing it,
        or None if this queue is empty."""
        if self.is_empty():
            return None
        return self.python3_dynamic_array[0]

    def dequeue(self):
        """Remove and return the item at the front of this queue,
        or raise ValueError if this queue is empty.
        Running time: O(n) – Why? There is the need to [TODO]"""
        if self.is_empty() is True:
            raise ValueError('There is not value to dequeue')
        return self.python3_dynamic_array.pop(0)


# Implement LinkedQueue and ArrayQueue above, then change the assignment below
# to use each of your Queue implementations to verify they each pass all tests
# Queue = LinkedQueue
Queue = ArrayQueue
