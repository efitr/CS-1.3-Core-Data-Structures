# aca se haran TODOS LOS TEST, 
# Seras los mejores jamas hechos
from set_array import Set
import unittest

class SetTest(unittest.TestCase):

    def test_init(self):
        int_item = 123
        set_array = Set(int_item)
        assert set_array.dynamic_array is int_item