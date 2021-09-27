import unittest
from bloom_filter_bitarray import BloomFilter

class TestBloomFilter(unittest.TestCase):

    def test_bloom(self):
        bf = BloomFilter(32)

        bf.add("0123456789")
        bf.add("1234567890")
        bf.add("2345678901")
        bf.add("3456789012")
        bf.add("4567890123")
        bf.add("5678901234")
        bf.add("6789012345")
        bf.add("7890123456")
        bf.add("8901234567")
        bf.add("9012345678")

        self.assertEqual(bf.is_value('9012345678'), True)
        self.assertEqual(bf.is_value("1234567890"), True)
        self.assertEqual(bf.is_value("0187654322"), False)
