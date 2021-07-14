import unittest
import random
from linked_dummy_as_field import Node, LinkedList


class LinkedListTests(unittest.TestCase):

    def test_list_creation(self):
        test_list = LinkedList()
        node_1 = Node(1)
        node_2 = Node(2)
        node_3 = Node(3)
        test_list.add_in_tail(node_1)
        test_list.add_in_tail(node_2)
        test_list.add_in_tail(node_3)
        # test_list.print_all_nodes()

    def test_add_in_head(self):
        test_list = LinkedList()
        node_1 = Node(1)

        test_list.add_in_head(node_1)
        self.assertEqual(test_list.head.get_next(), node_1)
        self.assertEqual(test_list.tail.get_prev(), node_1)
        self.assertEqual(node_1.get_next(), None)
        self.assertEqual(node_1.get_prev(), None)

        node_2 = Node(2)
        test_list.add_in_head(node_2)
        self.assertEqual(test_list.head.get_next(), node_2)
        self.assertEqual(node_2.get_prev(), None)
        self.assertEqual(node_2.get_next(), node_1)
        self.assertEqual(node_1.get_prev(), node_2)

    def test_find(self):
        test_list = LinkedList()
        node_1 = Node(999)

        for i in range(10):
            test_list.add_in_tail(Node(random.randint(1, 99)))
        test_list.add_in_tail(node_1)
        for i in range(10):
            test_list.add_in_tail(Node(random.randint(1, 99)))

        find_node = test_list.find(999)
        self.assertEqual(find_node, node_1)

    def test_find_all(self):
        test_list_1 = LinkedList()
        node_1 = Node(555)
        node_2 = Node(555)
        node_3 = Node(555)

        for i in range(30):
            test_list_1.add_in_tail(Node(random.randint(1, 20)))

        test_list_1.add_in_tail(node_1)
        test_list_1.add_in_tail(node_2)
        test_list_1.add_in_tail(node_3)

        self.assertEqual(test_list_1.find_all(555),
                         [node_1, node_2, node_3])

    def test_length(self):
        test_list = LinkedList()
        for i in range(30):
            test_list.add_in_tail(Node(random.randint(1, 5)))
        length = test_list.len()
        self.assertEqual(length, 30)

    def test_clean(self):
        test_list = LinkedList()
        for i in range(10):
            test_list.add_in_tail(Node(123))
        test_list.clean()
        self.assertEqual(test_list.len(), 0)
        self.assertEqual(test_list.head.get_next(), None)
        self.assertEqual(test_list.tail.get_prev(), None)

    def test_delete(self):
        test_list = LinkedList()
        node_1 = Node(1)

        test_list.add_in_tail(node_1)
        test_list.delete(1)

        node_2 = Node(2)
        node_3 = Node(3)
        test_list.add_in_tail(node_1)
        test_list.add_in_tail(node_2)
        test_list.add_in_tail(node_3)
        test_list.delete(2)
        self.assertEqual(node_1.get_next(), node_3)
        self.assertEqual(node_3.get_prev(), node_1)

    def test_delete_all(self):
        test_list = LinkedList()
        node_1 = Node(1)
        node_2 = Node(2)
        test_list.add_in_tail(node_1)
        for _ in range(10):
            test_list.add_in_tail(Node(5))
        test_list.add_in_tail(node_2)
        test_list.delete(5, True)
        self.assertEqual(node_1.get_next(), node_2)
        self.assertEqual(node_2.get_prev(), node_1)

    def test_insert(self):
        test_list = LinkedList()
        node_1 = Node(1)
        node_2 = Node(2)
        node_3 = Node(3)
        test_list.add_in_tail(node_1)
        test_list.add_in_tail(node_3)
        test_list.insert(node_1, node_2)
        self.assertEqual(node_1.get_next(), node_2)
        self.assertEqual(node_2.get_next(), node_3)
        self.assertEqual(node_2.get_prev(), node_1)
        self.assertEqual(node_3.get_prev(), node_2)
        self.assertEqual(node_3.get_next(), None)