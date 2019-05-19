
from set_hashtable import SetHashTable
import unittest
# Python 2 and 3 compatibility: unittest module renamed this assertion method
if not hasattr(unittest.TestCase, 'assertCountEqual'):
    unittest.TestCase.assertCountEqual = unittest.TestCase.assertItemsEqual


class HashTableTest(unittest.TestCase):

    def test_init(self):
        set_ht = SetHashTable(5)
        # set_hashtable = Se
        assert len(set_ht.hashtable.buckets) == 5
        assert set_ht.size() == 0

    def test_all_members(self):
        set_ht = SetHashTable(5)
        assert set_ht.all_members() == []
        set_ht.insert('I', 1)
        assert set_ht.all_members() == [('I', 1)]
        set_ht.insert('V', 5)
        self.assertCountEqual(set_ht.all_members(), [('I', 1), ('V', 5)])

    def test_is_member(self):
        set_ht = SetHashTable(5)
        set_ht.insert('T', 1)
        set_ht.insert('Y', 5)
        set_ht.insert('J', 10)
        assert set_ht.is_member('T') is True
        assert set_ht.is_member('Y') is True
        assert set_ht.is_member('J') is True
        assert set_ht.is_member('A') is False

    def test_size(self):
        set_ht = SetHashTable(5)
        assert set_ht.size() == 0
        set_ht.insert('I', 1)
        assert set_ht.size() == 1
        set_ht.insert('V', 5)
        assert set_ht.size() == 2
        set_ht.insert('X', 10)
        assert set_ht.size() == 3

if __name__ == '__main__':
    unittest.main()
