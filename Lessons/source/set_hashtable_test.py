
from set_hashtable import SetHashTable
import unittest
# Python 2 and 3 compatibility: unittest module renamed this assertion method
if not hasattr(unittest.TestCase, 'assertCountEqual'):
    unittest.TestCase.assertCountEqual = unittest.TestCase.assertItemsEqual


class HashTableTest(unittest.TestCase):

    def test_init(self):
        set_ht = SetHashTable(5)
        assert len(set_ht.hashtable.buckets) == 5
        assert set_ht.size == 0

    def test_all_members_by_inserting(self):
        set_ht = SetHashTable(5)
        assert set_ht.all_members() == []
        set_ht.insert('I', 1)
        assert set_ht.all_members() == [('I', 1)]
        set_ht.insert('V', 5)
        self.assertCountEqual(set_ht.all_members(), [('I', 1), ('V', 5)])

    def test_all_members_by_inserting_and_deleting(self):
        set_ht = SetHashTable(5)
        
        assert set_ht.all_members() == []
        set_ht.insert('J', 3)
        assert set_ht.all_members() == [('J', 3)]
        set_ht.insert('T', 6)
        self.assertCountEqual(set_ht.all_members(), [('J', 3), ('T', 6)])

        set_ht.remove('J')
        assert set_ht.all_members() == [('T', 6)]
        set_ht.remove('T')
        self.assertCountEqual(set_ht.all_members(), [])

    def test_all_members_by_inserting_deleting_and_adding_already_inside_members(self):
        set_ht = SetHashTable(5)

        assert set_ht.all_members() == []
        set_ht.insert('Y', 7)
        assert set_ht.all_members() == [('Y', 7)]
        set_ht.insert('R', 1)
        self.assertCountEqual(set_ht.all_members(), [('Y', 7), ('R', 1)])

        assert set_ht.is_member('Y') == True
        assert set_ht.is_member('Q') == False
        set_ht.insert('Q', 1)
        self.assertCountEqual(set_ht.all_members(), [('Q', 1), ('Y', 7), ('R', 1)])

    def test_is_member(self):
        set_ht = SetHashTable(5)
        set_ht.insert('T', 1)
        set_ht.insert('Y', 5)
        set_ht.insert('J', 10)
        assert set_ht.is_member('T') is True
        assert set_ht.is_member('Y') is True
        assert set_ht.is_member('J') is True
        assert set_ht.is_member('A') is False

    def test_is_member_inserting_deleting(self):
        set_ht = SetHashTable(5)
        set_ht.insert('A', 1)
        set_ht.insert('B', 2)
        set_ht.insert('C', 3)
        assert set_ht.is_member('A') is True
        assert set_ht.is_member('B') is True
        assert set_ht.is_member('C') is True

        set_ht.remove('A')
        set_ht.remove('B')
        set_ht.remove('C')
        assert set_ht.is_member('A') is False
        assert set_ht.is_member('B') is False
        assert set_ht.is_member('C') is False

    def test_is_member_inserting_deleting_inserting(self):
        set_ht = SetHashTable(5)
        set_ht.insert('F', 8)
        set_ht.insert('G', 9)
        set_ht.insert('H', 12)
        assert set_ht.is_member('F') is True
        assert set_ht.is_member('G') is True
        assert set_ht.is_member('H') is True

        set_ht.remove('F')
        set_ht.remove('G')
        set_ht.remove('H')
        assert set_ht.is_member('F') is False
        assert set_ht.is_member('G') is False
        assert set_ht.is_member('H') is False

        set_ht.insert('U', 1)
        set_ht.insert('I', 2)
        set_ht.insert('O', 3)
        assert set_ht.is_member('U') is True
        assert set_ht.is_member('I') is True
        assert set_ht.is_member('O') is True

        assert set_ht.is_member('R') is False
        assert set_ht.is_member('Z') is False
        assert set_ht.is_member('V') is False

    def test_insert_using_contains(self):
        set_ht = SetHashTable(5)
        set_ht.insert('Y', 8)
        set_ht.insert('G', 9)
        assert set_ht.is_member('Y') is True
        assert set_ht.is_member('G') is True

    def test_insert_using_all_members(self):
        set_ht = SetHashTable(5)
        set_ht.insert('Y', 8)
        set_ht.insert('G', 9)
        self.assertCountEqual(set_ht.all_members(), [('Y', 8), ('G', 9)])

    def test_insert_using_size_property(self):
        set_ht = SetHashTable(5)
        set_ht.insert('Y', 8)
        assert set_ht.size == 1
        set_ht.insert('G', 9)
        assert set_ht.size == 2

    def test_insert_using_size_property_and_deleting(self):
        set_ht = SetHashTable(5)
        set_ht.insert('Y', 8)
        assert set_ht.size == 1
        set_ht.remove('Y')
        assert set_ht.size == 0

    def test_insert_using_size_property_deleting_and_contains(self):
        set_ht = SetHashTable(5)
        set_ht.insert('R', 1)
        assert set_ht.size == 1
        set_ht.remove('R')
        assert set_ht.size == 0
        assert set_ht.is_member('R') == False

        set_ht.insert('Y', 1)
        assert set_ht.size == 1
        assert set_ht.is_member('Y') == True

    def test_delete_using_size_property(self):
        set_ht = SetHashTable(5)
        set_ht.insert('Y', 8)
        assert set_ht.size == 1
        set_ht.insert('G', 9)
        assert set_ht.size == 2

        set_ht.remove('Y')
        assert set_ht.size == 1
        set_ht.remove('G')
        assert set_ht.size == 0

    def test_delete_using_size_is_member(self):
        set_ht = SetHashTable(5)
        set_ht.insert('Y', 8)
        assert set_ht.is_member('Y') == True
        set_ht.insert('G', 9)
        assert set_ht.is_member('G') == True

        set_ht.remove('Y')
        assert set_ht.is_member('Y') == False
        set_ht.insert('B', 9)
        assert set_ht.is_member('G') == True

    def test_delete_using_all_members(self):
        set_ht = SetHashTable(5)

        set_ht.insert('Y', 8)
        self.assertCountEqual(set_ht.all_members(), [('Y', 8)])
        set_ht.insert('G', 9)
        self.assertCountEqual(set_ht.all_members(), [('Y', 8), ('G', 9)])

        set_ht.remove('Y')
        self.assertCountEqual(set_ht.all_members(), [('G', 9)])
        set_ht.remove('G')
        self.assertCountEqual(set_ht.all_members(), [])

    def test_size(self):
        set_ht = SetHashTable(5)
        assert set_ht.size == 0
        set_ht.insert('I', 1)
        assert set_ht.size == 1
        set_ht.insert('V', 5)
        assert set_ht.size == 2
        set_ht.insert('X', 10)
        assert set_ht.size == 3
    
    def test_lenght(self):
        set_ht = SetHashTable(5)
        assert set_ht.length() == 0
        set_ht.insert('I', 1)
        assert set_ht.length() == 1
        set_ht.insert('V', 5)
        assert set_ht.length() == 2
        set_ht.insert('X', 10)
        assert set_ht.length() == 3

if __name__ == '__main__':
    unittest.main()
