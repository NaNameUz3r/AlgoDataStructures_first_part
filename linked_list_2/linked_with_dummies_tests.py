import unittest
import random
from linked_with_dummies import Node, LinkedList


class LinkedListTest(unittest.TestCase):

    def test_add_in_tail(self):
        test_list = LinkedList()
        node_1 = Node(1)
        node_2 = Node(2)

        test_list.add_in_tail(node_1)
        self.assertEqual(test_list.dummy_head.next, node_1)
        self.assertEqual(test_list.dummy_tail.prev, node_1)

        test_list.add_in_tail(node_2)
        self.assertEqual(node_1.next, node_2)
        self.assertEqual(node_2.next, test_list.dummy_tail)
        self.assertEqual(test_list.dummy_tail.prev, node_2)

    def test_add_in_head(self):
        test_list = LinkedList()
        node_1 = Node(1)
        node_2 = Node(2)
        test_list.add_in_head(node_1)

        self.assertEqual(test_list.dummy_head.next, node_1)
        self.assertEqual(test_list.dummy_tail.prev, node_1)
        self.assertEqual(node_1.prev, test_list.dummy_head)
        self.assertEqual(node_1.next, test_list.dummy_tail)

        test_list.add_in_head(node_2)
        self.assertEqual(test_list.dummy_head.next, node_2)
        self.assertEqual(node_2.prev, test_list.dummy_head)
        self.assertEqual(node_2.next, node_1)
        self.assertEqual(node_1.prev, node_2)
        self.assertEqual(node_1.next, test_list.dummy_tail)

    def test_find(self):
        test_list = LinkedList()
        node_1 = Node(100)
        node_2 = Node(200)
        for i in range(10):
            test_list.add_in_head(Node(random.randint(1,10)))

        test_list.add_in_tail(node_1)
        test_list.add_in_head(node_2)
        find_100 = test_list.find(100)
        find_200 = test_list.find(200)
        self.assertEqual(node_1, find_100)
        self.assertEqual(node_2, find_200)

    def test_find_all(self):
        test_list = LinkedList()
        node_to_find_1 = Node(3)
        node_to_find_2 = Node(3)
        node_to_find_3 = Node(3)

        for i in range(3):
            test_list.add_in_tail(Node(random.randint(5, 10)))
        test_list.add_in_tail(node_to_find_1)
        for i in range(3):
            test_list.add_in_tail(Node(random.randint(5, 10)))
        test_list.add_in_tail(node_to_find_2)
        for i in range(3):
            test_list.add_in_tail(Node(random.randint(5, 10)))
        test_list.add_in_tail(node_to_find_3)

        nodes = [node_to_find_1, node_to_find_2, node_to_find_3]
        self.assertEqual(test_list.find_all(3), nodes)

    def test_delete_one_node(self):
        test_list = LinkedList()
        node_1 = Node(1)
        node_2 = Node(2)
        node_3 = Node(3)

        test_list.add_in_tail(node_1)
        test_list.add_in_tail(node_2)
        test_list.add_in_tail(node_3)

        test_list.delete(3)
        self.assertEqual(test_list.dummy_tail.prev, node_2)
        self.assertEqual(node_2.next, test_list.dummy_tail)

        test_list.delete(1)
        self.assertEqual(test_list.dummy_head.next, node_2)

        test_list.delete(2)
        self.assertEqual(test_list.dummy_head.next, test_list.dummy_tail)
        self.assertEqual(test_list.dummy_tail.prev, test_list.dummy_head)

        test_list.add_in_tail(node_1)
        test_list.add_in_tail(node_2)
        test_list.add_in_tail(node_3)

        test_list.delete(2)

        self.assertEqual(node_1.next, node_3)
        self.assertEqual(node_3.prev, node_1)

    def test_delete_by_value(self):
        test_list = LinkedList()
        node_1 = Node(1)
        node_2 = Node(2)
        node_3 = Node(3)

        test_list.add_in_tail(node_1)
        test_list.add_in_tail(node_2)
        test_list.add_in_tail(Node(2))
        test_list.add_in_tail(Node(2))
        test_list.add_in_tail(Node(2))
        test_list.add_in_tail(Node(2))
        test_list.add_in_tail(node_3)

        test_list.delete(2, True)
        self.assertEqual(test_list.dummy_head.next, node_1)

        test_list.add_in_head(Node(1))
        test_list.add_in_head(Node(1))
        test_list.add_in_head(Node(1))
        test_list.delete(1, True)

        self.assertEqual(test_list.dummy_head.next, node_3)
        self.assertEqual(test_list.dummy_tail.prev, node_3)
        self.assertEqual(node_3.next, test_list.dummy_tail)

        test_list.delete(3, True)

        self.assertEqual(test_list.dummy_head.next, test_list.dummy_tail)
        self.assertEqual(test_list.dummy_tail.prev, test_list.dummy_head)

    def test_clean(self):
        test_list = LinkedList()
        for i in range(10):
            test_list.add_in_tail(Node(random.randint(1,200)))
        test_list.clean()
        self.assertEqual(test_list.dummy_head.next, test_list.dummy_tail)
        self.assertEqual(test_list.dummy_tail.prev, test_list.dummy_head)

    def test_len(self):
        test_list = LinkedList()
        for i in range(10):
            test_list.add_in_head(Node(1))
        self.assertEqual(test_list.len(), 10)

    def test_insert(self):
        test_list = LinkedList()
        node_1 = Node(1)
        node_2 = Node(2)
        node_3 = Node(3)
        test_list.add_in_tail(node_3)
        test_list.add_in_head(node_2)
        test_list.add_in_head(node_1)

        node_333 = Node(333)
        test_list.insert(node_1, node_333)
        self.assertEqual(node_333.prev, node_1)
        self.assertEqual(node_333.next, node_2)
        self.assertEqual(node_2.prev, node_333)

        node_444 = Node(444)
        test_list.insert(node_3, node_444)

        self.assertEqual(node_444.prev, node_3)
        self.assertEqual(node_444.next, test_list.dummy_tail)
        self.assertEqual(test_list.dummy_tail.prev, node_444)
