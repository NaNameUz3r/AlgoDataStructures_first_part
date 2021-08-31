import unittest
from native_dictionary import NativeDictionary

class NativeDictTests(unittest.TestCase):

    def test_native_dictionary(self):
        nd = NativeDictionary(5)
        self.assertEqual(nd.is_key("hello"), False)
        nd.put("hello", "world")
        self.assertEqual(nd.is_key("hello"), True)
        self.assertEqual(nd.get("hello"), "world")
        self.assertEqual(nd.get("bye"), None)
        nd.put("hello", "friend")
        self.assertEqual(nd.get("hello"), "world")