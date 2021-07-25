from postfix_calculator import postfix_calculator
import unittest


class PostfixCalcTest(unittest.TestCase):

    def test_calculation(self):
        postfix_expression = '8 2 + 5 * 9 + ='
        self.assertEqual(postfix_calculator(postfix_expression), 59)
