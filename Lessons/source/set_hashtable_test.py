
from set_hashtable import SetHashTable
import unittest
# Python 2 and 3 compatibility: unittest module renamed this assertion method
if not hasattr(unittest.TestCase, 'assertCountEqual'):
    unittest.TestCase.assertCountEqual = unittest.TestCase.assertItemsEqual


class HashTableTest(unittest.TestCase):

    def test_init(self):
        set_ht = SetHashTable(4)
        # set_hashtable = Se
        assert len(set_ht.hashtable.buckets) == 5
        assert set_ht.size() == 0
        # assert set_ht.size == 0

    # def test_all_members(self):
    #     ht = HashTable()
    #     assert ht.items() == []
    #     ht.set('I', 1)
    #     assert ht.items() == [('I', 1)]
    #     ht.set('V', 5)
    #     self.assertCountEqual(ht.items(), [('I', 1), ('V', 5)])
    #     ht.set('X', 10)
    #     self.assertCountEqual(ht.items(), [('I', 1), ('V', 5), ('X', 10)])

    # def test_length(self):
    #     ht = HashTable()
    #     assert ht.length() == 0
    #     ht.set('I', 1)
    #     assert ht.length() == 1
    #     ht.set('V', 5)
    #     assert ht.length() == 2
    #     ht.set('X', 10)
    #     assert ht.length() == 3

    # def test_size(self):
    #     ht = HashTable()
    #     assert ht.size == 0
    #     ht.set('I', 1)
    #     assert ht.size == 1
    #     ht.set('V', 5)
    #     assert ht.size == 2
    #     ht.set('X', 10)
    #     assert ht.size == 3

if __name__ == '__main__':
    unittest.main()
