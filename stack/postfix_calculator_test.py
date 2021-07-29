from postfix_calculator import postfix_calculator
import unittest


class PostfixCalcTest(unittest.TestCase):

    def test_calculation(self):
        postfix_expression_1 = '8 2 + 5 * 9 + ='
        self.assertEqual(postfix_calculator(postfix_expression_1), 59)

        postfix_expression_2 = '10 5 - 20 + ='
        self.assertEqual(postfix_calculator(postfix_expression_2), 15)

        postfix_expression_3 = '10 5 - ='
        self.assertEqual(postfix_calculator(postfix_expression_3), -5)
