import unittest
import random
from native_cache import NativeCache


class TestNativeCache(unittest.TestCase):

    def test_basic_methods(self):
        nc = NativeCache(10, 3)

        key_1, value_1 = "hello", "friend"
        nc.put(key_1, value_1)
        for i in range(10):
            nc.get("hello")
        slot_index = nc.find_slot("hello")
        self.assertEqual(nc.hits[slot_index], 10)

    def test_slot_displace(self):
        nc = NativeCache(10, 3)
        key_1, value_1 = "hello", "friend"
        for i in range(500):
            nc.put(random.randint(0, 300), random.randint(1, 99))
        for j in range(nc.size):
            nc.hits[j] = random.randint(1, 999)

        less_hits = nc.define_displace_slot()
        less_hits_min_method = nc.hits.index(min(nc.hits))
        self.assertEqual(less_hits_min_method, less_hits)

        nc.put(key_1, value_1)
        self.assertEqual(nc.values[less_hits], value_1)