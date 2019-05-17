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

    def __init__(self, data=None):
        self.hashtable = HashTable()
        self.hashtable.buckets = [LinkedList() for i in range(5)]
        self.hashtable.size = 0
    
    def size(self):
        return self.hashtable.length()
        
    def all_members(self):
        return self.hashtable.items()

    def is_member(self, key):
        return self.hashtable.contains(key)

    def insert(self, key, value):
        if self.is_member(key) is not True:
            self.hashtable.set(key, value)
        raise ValueError('Item is already a member: {}'.format(item))
    
    def union(self, other_set):
        pass


    def intersection(self, other_set):
        pass

    def subset(self, other_set):
        pass

    def symmetric_difference(self, other_set):
        pass

    
    