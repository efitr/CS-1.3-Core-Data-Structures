###########################################################################
##### SET made using an dynamic array, called list in Python3
###########################################################################
class Set(object):
    # When the set gets initialized with items, 
    def __init__(self, items = None):
        self.members = []
        self.size = 0

        # On a set there is not many of any item
        if items is not None:

            for item in items:
                if self.contains(item) is False:
                    self.members.append(item)
                    self.size += 1

    
    def contains(self, item, index_of_found_member = None):
        # return a boolean indicating whether element is in this set
        index_of_member = 0
        for member in self.members: # O(n)
            if item is member:
                if index_of_found_member is True:
                    return True, index_of_member
                return True
            index_of_member += 1
        return False


    def add(self, item):
        # add element to this set, if not present already
        if self.contains(item) is False:
            self.members.append(item)
            self.size += 1
        return

    
    def remove(self, item):
        # remove element from this set, if present, or else raise KeyError
        if self.contains(item, True) is (True, index_of_found_member):
            self.dynamic_array.pop(index_of_found_member)
            return
        


        

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
