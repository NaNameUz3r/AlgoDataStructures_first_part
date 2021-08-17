import unittest
from deque import Deque
from deque_linkedlist import Deque as Deque2


class TestDeque(unittest.TestCase):

    def test_deque(self):
        deq = Deque()

        self.assertEqual(deq.size(), 0)
        deq.addFront("f1")
        self.assertEqual(deq.size(), 1)
        deq.addTail("t1")
        self.assertEqual(deq.size(), 2)
        deq.addFront("f2")
        self.assertEqual(deq.size(), 3)
        deq.addTail("t2")
        self.assertEqual(deq.size(), 4)

        self.assertEqual(deq.removeTail(), 't2')
        self.assertEqual(deq.size(), 3)
        self.assertEqual(deq.removeFront(), 'f2')
        self.assertEqual(deq.size(), 2)
        self.assertEqual(deq.removeFront(), 'f1')
        self.assertEqual(deq.removeFront(), 't1')
        self.assertEqual(deq.size(), 0)


class TestDequeLinkedList(unittest.TestCase):

    def test_deque(self):
        deq = Deque2()

        self.assertEqual(deq.size(), 0)
        deq.addFront("f1")
        self.assertEqual(deq.size(), 1)
        deq.addTail("t1")
        self.assertEqual(deq.size(), 2)
        deq.addFront("f2")
        self.assertEqual(deq.size(), 3)
        deq.addTail("t2")
        self.assertEqual(deq.size(), 4)

        self.assertEqual(deq.removeTail(), 't2')
        self.assertEqual(deq.size(), 3)
        self.assertEqual(deq.removeFront(), 'f2')
        self.assertEqual(deq.size(), 2)
        self.assertEqual(deq.removeTail(), 't1')
        self.assertEqual(deq.removeTail(), 'f1')
        self.assertEqual(deq.size(), 0)
