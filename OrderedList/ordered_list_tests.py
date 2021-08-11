import unittest
from ordered_list import OrderedList,Node


class TestOrderedList(unittest.TestCase):

    def test_asc_methods(self):
        ol = OrderedList()

        # test add method

        ol.add(5)
        ol.add(2)
        self.assertEqual(ol.head.value, 2)
        self.assertEqual(ol.head.next.value, 5)
        self.assertEqual(ol.head.prev, None)
        self.assertEqual(ol.tail.value, 5)
        self.assertEqual(ol.tail.prev.value, 2)
        self.assertEqual(ol.tail.next, None)
        self.assertEqual(ol.len(), 2)

        ol.add(3)
        self.assertEqual(ol.head.next.value, 3)
        self.assertEqual(ol.head.next.next, ol.tail)
        self.assertEqual(ol.tail.prev.value, 3)

        # test find method
        self.assertEqual(ol.find(2), ol.head)
        self.assertEqual(ol.find(3), ol.head.next)
        self.assertEqual(ol.find(5), ol.tail)
        self.assertEqual(ol.len(), 3)

        # test get_all method
        ol_list = [ol.head, ol.head.next, ol.tail]
        self.assertEqual(ol.get_all(), ol_list)

        # test delete method
        ol.delete(2)
        self.assertEqual(ol.len(), 2)
        self.assertEqual(ol.head.value, 3)
        self.assertEqual(ol.tail.value, 5)
        self.assertEqual(ol.head.prev, None)
        self.assertEqual(ol.head.next, ol.tail)
        self.assertEqual(ol.tail.prev, ol.head)

        ol.delete(3)
        ol.delete(5)
        self.assertEqual(ol.len(), 0)
        self.assertEqual(ol.head, None)
        self.assertEqual(ol.tail, None)

    def test_desc_methods(self):
        ol = OrderedList(False)

        # test add method

        ol.add(5)
        ol.add(2)
        self.assertEqual(ol.head.value, 5)
        self.assertEqual(ol.head.next.value, 2)
        self.assertEqual(ol.head.prev, None)
        self.assertEqual(ol.tail.value, 2)
        self.assertEqual(ol.tail.prev.value, 5)
        self.assertEqual(ol.tail.next, None)
        self.assertEqual(ol.len(), 2)

        ol.add(3)
        self.assertEqual(ol.head.next.value, 3)
        self.assertEqual(ol.head.next.next, ol.tail)
        self.assertEqual(ol.tail.prev.value, 3)

        # test find method
        self.assertEqual(ol.find(2), ol.tail)
        self.assertEqual(ol.find(3), ol.head.next)
        self.assertEqual(ol.find(5), ol.head)
        self.assertEqual(ol.len(), 3)

        # test get_all method
        ol_list = [ol.head, ol.head.next, ol.tail]
        self.assertEqual(ol.get_all(), ol_list)

        ol.delete(2)
        self.assertEqual(ol.len(), 2)
        self.assertEqual(ol.tail.value, 3)
        self.assertEqual(ol.head.value, 5)
        self.assertEqual(ol.head.prev, None)
        self.assertEqual(ol.head.next, ol.tail)
        self.assertEqual(ol.tail.prev, ol.head)
        ol.delete(3)
        ol.delete(5)
        self.assertEqual(ol.len(), 0)
        self.assertEqual(ol.head, None)
        self.assertEqual(ol.tail, None)
