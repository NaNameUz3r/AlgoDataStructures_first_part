import unittest
import random
from hash_table import HashTable


class HashTableTests(unittest.TestCase):

    def test_hash_table(self):
        hs = HashTable(17, 3)

        for i in range(10):
            hs.put(str(random.randint(1, 99999)))

        test_value = 'hello friend'
        hs.put(test_value)
        self.assertEqual(hs.find(test_value), hs.slots.index(test_value))