import unittest
import random
from linked_list_2 import Node, LinkedList2


class LinkedListTests(unittest.TestCase):

    def test_list_creation(self):
        test_list = LinkedList2()
        node_1 = Node(1)
        node_2 = Node(2)
        node_3 = Node(3)
        test_list.add_in_tail(node_1)
        test_list.add_in_tail(node_2)
        test_list.add_in_tail(node_3)
        test_list.add_in_tail(Node(4))
        test_list.add_in_tail(Node(4))
        test_list.add_in_tail(Node(4))

    def test_delete_one_node(self):
        test_list = LinkedList2()
        node_1 = Node(1)
        node_2 = Node(2)
        node_3 = Node(3)

        test_list.add_in_tail(node_1)
        test_list.add_in_tail(node_2)
        test_list.add_in_tail(node_3)

        test_list.delete(3)
        self.assertEqual(test_list.head, node_1)
        self.assertEqual(test_list.head.prev, None)
        self.assertEqual(test_list.tail, node_2)
        self.assertEqual(test_list.tail.next, None)
        self.assertEqual(test_list.tail.prev, node_1)

        test_list.delete(1)

        self.assertEqual(test_list.head, node_2)
        self.assertEqual(test_list.tail, node_2)
        self.assertEqual(test_list.head, test_list.tail)
        self.assertEqual(test_list.head.next, None)
        self.assertEqual(test_list.tail.prev, None)


        test_list.delete(2)
        self.assertEqual(test_list.head, None)
        self.assertEqual(test_list.tail, None)

        test_list.add_in_tail(node_1)
        test_list.add_in_tail(node_2)
        test_list.add_in_tail(node_3)

        test_list.delete(2)

        self.assertEqual(node_1.next, node_3)
        self.assertEqual(node_3.prev, node_1)

    def test_delete_by_value(self):
        test_list = LinkedList2()
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
        self.assertEqual(test_list.head.value, 1)
        self.assertEqual(test_list.head.next, node_3)
        self.assertEqual(test_list.head.prev, None)
        self.assertEqual(test_list.tail.value, 3)
        self.assertEqual(test_list.tail.prev, node_1)

        test_list.clean()

        test_list.add_in_tail(node_1)
        for i in range(10):
            test_list.add_in_tail(Node(1))
        test_list.add_in_tail(Node(2))
        test_list.add_in_tail(Node(3))
        test_list.delete(1, True)

        self.assertEqual(test_list.head.value, 2)
        self.assertEqual(test_list.tail.value, 3)

    def test_len_method(self):
        test_list = LinkedList2()
        for node in range(10):
            test_list.add_in_tail(Node(random.randint(1, 100)))

        self.assertEqual(test_list.len(), 10)

    def test_insert_in_empty(self):
        test_list = LinkedList2()
        test_list.insert(None, Node(666))
        self.assertEqual(test_list.head.value, 666)
        self.assertEqual(test_list.head.prev, None)
        self.assertEqual(test_list.tail.value, 666)
        self.assertEqual(test_list.tail.next, None)

    def test_insert(self):
        test_list = LinkedList2()
        node_1 = Node(1)
        node_2 = Node(2)
        node_3 = Node(3)

        test_list.add_in_tail(node_1)
        test_list.add_in_tail(node_2)
        test_list.add_in_tail(node_3)

        node_999 = Node(999)
        test_list.insert(None, node_999)

        self.assertEqual(test_list.tail.value, 999)
        self.assertEqual(test_list.tail.next, None)
        self.assertEqual(test_list.tail.prev, node_3)
        self.assertEqual(node_3.next, test_list.tail)

        node_555 = Node(555)
        test_list.insert(node_1, node_555)
        self.assertEqual(node_1.next, node_555)
        self.assertEqual(node_555.prev, node_1)
        self.assertEqual(node_555.next, node_2)

        node_1000 = Node(1000)
        test_list.insert(node_999, node_1000)
        self.assertEqual(test_list.tail, node_1000)
        self.assertEqual(node_999.next, node_1000)
        self.assertEqual(node_1000.next, None)
        self.assertEqual(node_1000.prev, node_999)

    def test_add_in_tail(self):
        test_list = LinkedList2()
        node_1 = Node(1)
        node_2 = Node(2)
        node_3 = Node(3)
        test_list.add_in_tail(node_1)
        test_list.add_in_tail(node_2)
        test_list.add_in_tail(node_3)

        self.assertEqual(test_list.head, node_1)
        self.assertEqual(test_list.tail, node_3)
        self.assertEqual(test_list.head.prev, None)
        self.assertEqual(test_list.tail.next, None)

        self.assertEqual(node_1.next, node_2)
        self.assertEqual(node_2.prev, node_1)
        self.assertEqual(node_2.next, node_3)
        self.assertEqual(node_3.prev, node_2)


    def test_add_head(self):
        test_list = LinkedList2()
        node_1 = Node(1)
        node_2 = Node(2)
        node_3 = Node(3)
        test_list.add_in_tail(node_1)
        test_list.add_in_tail(node_2)
        test_list.add_in_tail(node_3)

        node_0 = Node(0)
        test_list.add_in_head(node_0)
        self.assertEqual(test_list.head, node_0)
        self.assertEqual(node_0.next, node_1)
        self.assertEqual(node_0.prev, None)

    def test_find(self):
        test_list = LinkedList2()
        node_to_find = Node(3)
        for i in range(5):
            test_list.add_in_tail(Node(random.randint(1, 99)))
        test_list.add_in_tail(node_to_find)
        for i in range(5):
            test_list.add_in_tail(Node(random.randint(1, 99)))

        find_3 = test_list.find(3)
        self.assertEqual(node_to_find, find_3)

    def test_find_add(self):
        test_list = LinkedList2()
        node_to_find_1 = Node(3)
        node_to_find_2 = Node(3)
        node_to_find_3 = Node(3)
        for i in range(5):
            test_list.add_in_tail(Node(random.randint(1, 99)))
        test_list.add_in_tail(node_to_find_1)
        for i in range(5):
            test_list.add_in_tail(Node(random.randint(1, 99)))
        test_list.add_in_tail(node_to_find_2)
        for i in range(5):
            test_list.add_in_tail(Node(random.randint(1, 99)))
        test_list.add_in_tail(node_to_find_3)

        nodes = [node_to_find_1, node_to_find_2, node_to_find_3]
        find_nodes = test_list.find_all(3)
        self.assertEqual(find_nodes, nodes)

