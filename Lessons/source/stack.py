#!python

from linkedlist import LinkedList


# Implement LinkedStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class LinkedStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new linked list to store the items
        self.linked_list = LinkedList()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        # TODO: Check if empty
        if self.linked_list.size == 0:
            return True
        else:
            return False

    def length(self):
        """Return the number of items in this stack."""
        return self.linked_list.size

    def push(self, item):
        """Insert the given item on the top of this stack.
        Running time: O(???) – Why? [TODO]"""
        self.linked_list.prepend(item) 

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""
        if self.linked_list.is_empty():
            return None
        else:
            return self.linked_list.get_at_index(0)

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty.
        Running time: O(???) – Why? [TODO]"""
        if not self.linked_list.is_empty():
            item = self.linked_list.head.data
            self.linked_list.delete(item)
            return item
        else:
            raise ValueError('The stack is empty')


# Implement ArrayStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class ArrayStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new list (dynamic array) to store the items
        self.python3_dynamic_array = list()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        if len(self.python3_dynamic_array) == 0:
            return True
        return False

    def length(self):
        """Return the number of items in this stack."""
        return len(self.python3_dynamic_array)

    def push(self, item):
        """Insert the given item on the top of this stack.
        Running time: O(1) – Why? You are always appending to the top of the meaning 
        end of the list [TODO]"""
        self.python3_dynamic_array.append(item)

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""
        if self.is_empty():
            return None
        return self.python3_dynamic_array[len(self.python3_dynamic_array)-1]

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty.
        Running time: O(???) – Why? [TODO]"""
        if self.is_empty():
            raise ValueError('The stack is empty')
        return self.python3_dynamic_array.pop()


# Implement LinkedStack and ArrayStack above, then change the assignment below
# to use each of your Stack implementations to verify they each pass all tests
Stack = LinkedStack
# Stack = ArrayStack
