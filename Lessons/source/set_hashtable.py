from hashtable import HashTable
from linkedlist import LinkedList, Node
# Set basic properties
    # * Size
# Set basic operations
    # * Insert
    # * Contains
    # * Remove
# Set properties operation
    # * Union
    # * Intersection
    # * Subset
    # * Symetric Difference

class SetHashTable(object):

    def __init__(self, init_size=None):
        self.hashtable = HashTable()
        self.hashtable.buckets = [LinkedList() for i in range(init_size)]
        self.size = 0
    
    def length(self):
        return self.hashtable.length()
        
    def all_members(self):
        return self.hashtable.items()

    def is_member(self, key):
        return self.hashtable.contains(key)

    def insert(self, key, value):
        if self.is_member(key) is True:
            raise ValueError('Item is already a member: {}'.format(key))
        self.hashtable.set(key, value)
        self.size += 1
    
    def remove(self, key):
        if self.is_member(key) is False:
            raise ValueError('Item is not a member: {}'.format(key))
        self.size -= 1
        return self.hashtable.delete(key)
    
    def union(self, some_set, other_set):
        new_set = SetHashTable(5)
        for index, member in some_set.all_members():
            new_set.insert(index, member)
        for index, member in other_set.all_members():
            new_set.insert(index, member)
        return new_set

    def intersection(self, some_set, other_set):
        # Must get both elements that intercept here
        new_set = SetHashTable(5)
        # Optimization for when some_set is longer or equally long
        if some_set.length() >= other_set.length():
            for key, member in some_set.all_members():
                if other_set.is_member(key):
                    new_set.insert(key, member)
            return new_set
        # Optimization for when other set is longer
        for key, member in other_set.all_members():
            if some_set.is_member(key):
                new_set.insert(key, member)
        return new_set

    def subset(self, other_set):
        pass

    def symmetric_difference(self, other_set):
        pass

    
    