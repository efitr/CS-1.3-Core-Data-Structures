###########################################################################
##### SET made using an dynamic array, called list in Python3
###########################################################################
class Set(object):
    # When the set gets initialized with items, 
    def __init__(self, items = None):
        self.dynamic_array = []
        self.size = 0

        # On a set there is not many of any item
        if items is not None:

            for item in items:
                if self.contains(item) is False:
                    self.dynamic_array.append(item)
                    self.size += 1

    # Return the current size of the Set
    def size(self):
        #property that tracks the number of items in constant time
        return self.size # O(1)
    
    # Return all the current members in the Set
    def members(self):
        return self.dynamic_array # O(1)

    
    def contains(self, item, something = None):
        # return a boolean indicating whether element is in this set
        index_of_found_member = 0
        for member in self.members: # O(n)
            if item is member:
                if index_of_found_member is something:
                    return True, index_of_found_member
                return True
            index_of_found_member += 1
        return False


    def add(self, item):
        # add element to this set, if not present already
        if self.contains(item) is False:
            self.dynamic_array.append(item)
            self.size += 1
        return

    
    def remove(self, item):
        # remove element from this set, if present, or else raise KeyError
        if self.contains(item, something) is (True, index_of_found_member):
            self.dynamic_array.pop()
            return
        

        self.members[self.size] = 
        

    def union(other_set):
        #return a new set that is the union of this set and other_set
        pass
    def intersection(other_set):
        #return a new set that is the intersection of this set and other_set
        #good comment says why not what
        pass
    def difference(other_set):
        #return a new set that is the difference of this set and other_set
        pass
    def is_subset(other_set):
        #return a boolean indicating whether other_set is a subset of this set
        pass
