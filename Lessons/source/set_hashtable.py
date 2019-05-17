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
        pass
        
    def all_members(self):
        return self.hashtable.items()

    def is_member(self, item):
        return self.hashtable.contains(item)

    def insert(self, item):
        pass
    
    def intersection(self, other_set):
        pass

    def union(self, other_set):
        pass

    def subset(self, other_set):
        pass

    def symetric_difference(self, other_set):
        pass

    
    