from check_balance import is_balanced
import unittest

class CheckBalanceTests(unittest.TestCase):

    def test_balance(self):
        string_1 = '(())()(())'     # True
        string_2 = '(()((())()))'   # True
        string_3 = '))(('           # False
        string_4 = '((())'          # False
        string_5 = '(()))'          # False

        self.assertEqual(is_balanced(string_1), True)
        self.assertEqual(is_balanced(string_2), True)
        self.assertEqual(is_balanced(string_3), False)
        self.assertEqual(is_balanced(string_4), False)
        self.assertEqual(is_balanced(string_5), False)