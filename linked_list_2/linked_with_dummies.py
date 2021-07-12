class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.dummy_head = Node(None)
        self.dummy_tail = Node(None)
        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head

    def print_all_nodes(self):
        node = self.dummy_head.next
        while node != self.dummy_tail:
            print(node.value)
            node = node.next

    def add_in_tail(self, new_node):
        if self.dummy_head.next == self.dummy_tail:
            self.dummy_head.next = new_node
            new_node.next = self.dummy_tail
            new_node.prev = self.dummy_head
            self.dummy_tail.prev = new_node
        else:
            self.dummy_tail.prev.next = new_node
            new_node.prev = self.dummy_tail.prev
            new_node.next = self.dummy_tail
            self.dummy_tail.prev = new_node

    def add_in_head(self, new_node):
        if self.dummy_head.next == self.dummy_tail:
            self.dummy_head.next = new_node
            new_node.next = self.dummy_tail
            new_node.prev = self.dummy_head
            self.dummy_tail.prev = new_node
        else:
            new_node.next = self.dummy_head.next
            self.dummy_head.next.prev = new_node
            new_node.prev = self.dummy_head
            self.dummy_head.next = new_node

    def find(self, val):
        node = self.dummy_head.next
        while node is not self.dummy_head:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        found_nodes = []
        node = self.dummy_head.next
        while node is not self.dummy_tail:
            if node.value == val:
                found_nodes.append(node)
            node = node.next
        return found_nodes

    def delete(self, val, all=False):
        node = self.dummy_head.next

        if all:
            while node is not self.dummy_tail:
                if node.value == val:
                    node.next.prev = node.prev
                    node.prev.next = node.next
                node = node.next
        else:
            while node.value != val:
                node = node.next
            if node.value == val:
                node.prev.next = node.next
                node.next.prev = node.prev

    def clean(self):
        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head

    def len(self):
        node = self.dummy_head.next
        items_counter = 0
        while node != self.dummy_tail:
            items_counter += 1
            node = node.next
        return items_counter

    def insert(self, afterNode, newNode):
        node = self.dummy_head.next
        while node != afterNode:
            node = node.next
        if node == afterNode:
            node.next.prev = newNode
            newNode.next = node.next
            newNode.prev = node
            node.next = newNode
