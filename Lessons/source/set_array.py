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
    # def contains(self, item):
        # return a boolean indicating whether element is in this set
        if index_of_found_member is not None:
            for index in range(self.size):
                if self.members[index] is item:
                    return True, index
            return False
                
        for member in self.members: # O(n)
            if item is member:
                return True
        return False


    def add(self, item):
        # add element to this set, if not present already
        if self.contains(item) is False:
            self.members.append(item)
            self.size += 1
        return

    
    def remove(self, item):
        
        # remove element from this set, if present, or else raise KeyError
        if self.contains(item, index_of_found_member) is not False:
            self.members.pop([index_of_member])
        raise ValueError('This item is not a member of this set: {}'.format(item))
        pass


        

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
