from queue import Queue
from spinning_queue import spin_queue
from two_stacks_queue import TwoStackQueue
import unittest


class TestQueue(unittest.TestCase):

    def test_queue(self):
        qu = Queue()
        qu.enqueue(1)
        qu.enqueue(2)
        qu.enqueue(3)
        self.assertEqual(qu.size(), 3)

        self.assertEqual(qu.dequeue(), 1)
        self.assertEqual(qu.dequeue(), 2)
        self.assertEqual(qu.dequeue(), 3)

        self.assertEqual(qu.size(), 0)


class TestSpinFunc(unittest.TestCase):

    def test_spin_func(self):

        qu = Queue()
        qu.enqueue(1)
        qu.enqueue(2)
        qu.enqueue(3)

        spin_queue(qu, 2)

        self.assertEqual(qu.dequeue(), 3)
        self.assertEqual(qu.dequeue(), 1)
        self.assertEqual(qu.dequeue(), 2)


class TestTwoStackQueue(unittest.TestCase):

    def test_two_stacks(self):

        qu = TwoStackQueue()
        qu.enqueue(1)
        qu.enqueue(2)
        qu.enqueue(3)

        self.assertEqual(qu.size(), 3)

        self.assertEqual(qu.dequeue(), 1)
        self.assertEqual(qu.dequeue(), 2)
        self.assertEqual(qu.dequeue(), 3)

        self.assertEqual(qu.size(), 0)
