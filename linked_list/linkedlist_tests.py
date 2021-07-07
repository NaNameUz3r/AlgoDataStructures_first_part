import unittest
import random
from linked_list import Node, LinkedList


class LinkedListTests(unittest.TestCase):

    def test_list_creation(self):
        test_list = LinkedList()
        node_1 = Node(1)
        node_2 = Node(2)
        node_3 = Node(3)
        test_list.add_in_tail(node_1)
        test_list.add_in_tail(node_2)
        test_list.add_in_tail(node_3)
        test_list.add_in_tail(Node(4))

        self.assertEqual(test_list.head.value, 1)
        self.assertEqual(test_list.tail.value, 4)
        self.assertEqual(test_list.tail.next, None)

    def test_clean(self):
        test_list = LinkedList()

        for i in range(20):
            test_list.add_in_tail(Node(random.randint(1, 100)))

        test_list.clean()

        self.assertEqual(test_list.head, None)
        self.assertEqual(test_list.tail, None)
        self.assertEqual(test_list.print_all_nodes(), None)

    def test_len(self):
        test_list = LinkedList()
        self.assertEqual(test_list.len(), 0)
        for i in range(10):
            test_list.add_in_tail(Node(random.randint(1, 999)))
        self.assertEqual(test_list.len(), 10)

    def test_delete_one_element(self):
        test_list = LinkedList()

        test_list.delete(100)
        node_1 = Node(1)
        node_2 = Node(2)
        node_3 = Node(3)
        test_list.add_in_tail(node_1)
        test_list.add_in_tail(node_2)
        test_list.add_in_tail(node_3)
        test_list.add_in_tail(Node(4))
        test_list.delete(1)
        test_list.delete(4)

        self.assertEqual(test_list.head.value, 2)
        self.assertEqual(test_list.tail.value, 3)
        self.assertEqual(test_list.tail.next, None)

        test_list.clean()
        test_list.add_in_tail(Node(1))
        test_list.delete(1)

        self.assertEqual(test_list.head, None)
        self.assertEqual(test_list.tail, None)
        self.assertEqual(test_list.print_all_nodes(), None)

    def test_delete_few_elements(self):
        test_list = LinkedList()
        node_1 = Node(1)
        node_3 = Node(3)
        node_4 = Node(4)

        test_list.add_in_tail(node_1)
        for i in range(10):
            test_list.add_in_tail(Node(2))
        test_list.add_in_tail(node_3)
        test_list.add_in_tail(node_4)

        test_list.delete(2, True)

        self.assertEqual(test_list.len(), 3)
        self.assertEqual(test_list.head.value, 1)
        self.assertEqual(test_list.head.next.value, 3)
        self.assertEqual(test_list.tail.value, 4)
        self.assertEqual(test_list.tail.next, None)

        test_list.delete(4, True)

        self.assertEqual(test_list.tail.value, 3)
        self.assertEqual(test_list.tail.next, None)

        test_list.delete(3, True)

        self.assertEqual(test_list.tail.value, 1)
        self.assertEqual(test_list.head.value, 1)
        self.assertEqual(test_list.tail.next, None)

        for i in range(10):
            test_list.add_in_tail(Node(1))

        test_list.delete(1, True)

        self.assertEqual(test_list.head, None)
        self.assertEqual(test_list.tail, None)
        self.assertEqual(test_list.len(), 0)

    def test_find_all(self):
        test_list = LinkedList()
        node_1 = Node(1)
        node_2 = Node(2)
        node_2_1 = Node(2)
        node_2_2 = Node(2)
        node_2_3 = Node(2)
        node_3 = Node(3)
        node_list = [node_2, node_2_1, node_2_2, node_2_3]

        test_list.add_in_tail(node_1)
        test_list.add_in_tail(node_2)
        test_list.add_in_tail(node_2_1)
        test_list.add_in_tail(node_2_2)
        test_list.add_in_tail(node_2_3)
        test_list.add_in_tail(node_3)

        self.assertEqual(test_list.find_all(2), node_list)

        test_list.clean()
        test_list.add_in_tail(node_3)
        self.assertEqual(test_list.find(3), node_3)
        self.assertEqual(test_list.find_all(3), [node_3])

    def test_insert(self):
        test_list = LinkedList()
        node_1 = Node(1)
        node_2 = Node(2)
        node_4 = Node(4)

        node_0 = Node(0)
        node_3 = Node(3)
        node_5 = Node(5)

        test_list.add_in_tail(node_1)
        test_list.add_in_tail(node_2)
        test_list.add_in_tail(node_4)

        test_list.insert(None, node_0)

        self.assertEqual(test_list.head.value, 0)
        self.assertEqual(test_list.head.next.value, 1)

        test_list.insert(node_2, node_3)

        self.assertEqual(node_2.next.value, node_3.value)
        self.assertEqual(node_3.next.value, node_4.value)

        test_list.insert(node_4, node_5)

        self.assertEqual(test_list.tail, node_5)
        self.assertEqual(node_4.next.value, node_5.value)
        self.assertEqual(node_5.next, None)


if __name__ == '__main__':
    unittest.main()
