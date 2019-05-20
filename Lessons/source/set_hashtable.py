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

    def all_keys(self):
        return self.hashtable.keys()
        
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
        for key, member in some_set.all_members():
            new_set.insert(key, member)
        for key, member in other_set.all_members():
            if new_set.is_member(key) is False:
                new_set.insert(key, member)
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

    def symmetric_difference(self, some_set, other_set):
        union_set = SetHashTable(5)
        union_set = union_set.union(some_set, other_set)

        intersection_set = SetHashTable(5)
        intersection_set = intersection_set.intersection(some_set, other_set)
        
        for key in intersection_set.all_keys():
            if union_set.is_member(key):
                union_set.remove(key)
        return union_set


        # Optimization to do the operation over the bigger set
        # if some_set.length() >= other_set.length():
        #     for key, member in some_set.all_members():
        #         if not other_set.is_member(key):
        #             new_set.insert(key, member)
        #     return new_set
        # # all 
        # for member in other_set.all_members():
        #     if not some_set.is_member(key):
        #         new_set.insert(key, member)
        # return new_set

        

    # Here you are seeing if the 
    def subset(self, other_set):
        for key in self.all_keys():
            if not other_set.is_member(key):
                return False
        return True