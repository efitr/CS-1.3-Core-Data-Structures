from set_hashtable import SetHashTable
import unittest
# Python 2 and 3 compatibility: unittest module renamed this assertion method
if not hasattr(unittest.TestCase, 'assertCountEqual'):
    unittest.TestCase.assertCountEqual = unittest.TestCase.assertItemsEqual


class HashTableTest(unittest.TestCase):

    def test_unions_small_sets(self):
        set_ht = SetHashTable(5)
        set_ht.insert('A', 5)

        other_set_ht = SetHashTable(5)
        other_set_ht.insert('T', 1)

        new_set = SetHashTable(5)
        new_set = new_set.union(set_ht, other_set_ht)

        assert new_set.size == 2


    def test_union_medium_sets(self):
        set_ht = SetHashTable(5)
        set_ht.insert('A', 5)
        set_ht.insert('B', 1)
        set_ht.insert('C', 4)
        
        other_set_ht = SetHashTable(5)
        other_set_ht.insert('T', 9)
        other_set_ht.insert('Y', 8)
        other_set_ht.insert('U', 7)

        new_set = SetHashTable(5)
        new_set = new_set.union(set_ht, other_set_ht)

        assert new_set.length() == 6


    def test_union_large_sets(self):
        set_ht = SetHashTable(5)
        set_ht.insert('A', 1)
        set_ht.insert('B', 2)
        set_ht.insert('C', 3)
        set_ht.insert('D', 4)
        set_ht.insert('E', 5)
        set_ht.insert('F', 6)
        
        other_set_ht = SetHashTable(5)
        other_set_ht.insert('G', 7)
        other_set_ht.insert('H', 8)
        other_set_ht.insert('I', 9)
        other_set_ht.insert('J', 10)
        other_set_ht.insert('K', 11)
        other_set_ht.insert('L', 12)
    
        new_set = SetHashTable(5)
        new_set = new_set.union(set_ht, other_set_ht)

        assert new_set.is_member('G') == True
        assert new_set.is_member('H') == True
        assert new_set.is_member('I') == True
        assert new_set.is_member('J') == True
        assert new_set.is_member('K') == True
        assert new_set.is_member('L') == True

        assert new_set.is_member('A') == True
        assert new_set.is_member('B') == True
        assert new_set.is_member('C') == True
        assert new_set.is_member('D') == True
        assert new_set.is_member('E') == True
        assert new_set.is_member('F') == True


    def test_intersection_small_sets(self):
        set_ht = SetHashTable(5)
        set_ht.insert('A', 5)

        other_set_ht = SetHashTable(5)
        other_set_ht.insert('T', 1)

        new_set = SetHashTable(5)
        new_set = new_set.intersection(set_ht, other_set_ht)

        assert new_set.size == 0

    def test_intersection_medium_sets(self):
        set_ht = SetHashTable(5)
        set_ht.insert('A', 5)
        set_ht.insert('B', 1)
        set_ht.insert('C', 4)
        
        other_set_ht = SetHashTable(5)
        other_set_ht.insert('A', 9)
        other_set_ht.insert('B', 8)
        other_set_ht.insert('U', 7)

        new_set = SetHashTable(5)
        new_set = new_set.intersection(set_ht, other_set_ht)

        assert new_set.length() == 2

    def test_intersection_large_sets(self):
        set_ht = SetHashTable(5)
        set_ht.insert('A', 1)
        set_ht.insert('B', 2)
        set_ht.insert('C', 3)
        set_ht.insert('D', 4)
        set_ht.insert('E', 5)
        set_ht.insert('F', 6)
        
        other_set_ht = SetHashTable(5)
        other_set_ht.insert('G', 7)
        other_set_ht.insert('H', 8)
        other_set_ht.insert('I', 9)
        other_set_ht.insert('D', 10)
        other_set_ht.insert('E', 11)
        other_set_ht.insert('F', 12)
    
        new_set = SetHashTable(5)
        new_set = new_set.intersection(set_ht, other_set_ht)

        assert new_set.is_member('D') == True
        assert new_set.is_member('E') == True
        assert new_set.is_member('F') == True
        assert new_set.is_member('J') == False
        assert new_set.is_member('K') == False
        assert new_set.is_member('L') == False

    
    # def test_symetric_difference_small_sets(self):
    #     set_ht = SetHashTable()

    #     other_set_ht = SetHashTable()

    # def test_symetric_difference_medium_sets(self):
    #     set_ht = SetHashTable()

    #     other_set_ht = SetHashTable()

    # def test_symetric_difference_large_sets(self):
    #     set_ht = SetHashTable()

    #     other_set_ht = SetHashTable()

    
    # def test_is_subset_small_sets(self):
    #     set_ht = SetHashTable()

    #     other_set_ht = SetHashTable()

    # def test_is_subset_medium_sets(self):
    #     set_ht = SetHashTable()

    #     other_set_ht = SetHashTable()

    # def test_is_subset_large_sets(self):
    #     set_ht = SetHashTable()

    #     other_set_ht = SetHashTable()


if __name__ == '__main__':
    unittest.main()
