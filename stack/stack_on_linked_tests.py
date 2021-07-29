import unittest
from stack_on_linked import Stack


class StackTests(unittest.TestCase):

    def test_stack(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)

        self.assertEqual(stack.size(), 3)
        self.assertEqual(stack.peek(), 3)

        stack.pop()
        self.assertEqual(stack.size(), 2)
        self.assertEqual(stack.peek(), 2)

        stack.pop()

        stack.pop()

        self.assertEqual(stack.size(), 0)
        self.assertEqual(stack.pop(), None)
        self.assertEqual(stack.peek(), None)

    def test_stack_pop_one_element(self):
        stack = Stack()
        stack.push(1)
        self.assertEqual(stack.size(), 1)
        x = stack.pop()
        self.assertEqual(x, 1)
        self.assertEqual(stack.size(), 0)