class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class LinkedList2:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        found_nodes = []
        node = self.head
        while node is not None:
            if node.value == val:
                found_nodes.append(node)
            node = node.next
        return found_nodes

    def delete(self, val, all=False):
        node = self.head

        if self.tail is None and self.head is None:
            return None

        if self.head == self.tail:
            self.head.next = None
            self.tail.prev = None

        if all:
            while node is not None:
                if node.next == self.tail and self.tail.value != val:
                    return
                if node.value == val and node == self.head:
                    self.head = node.next
                    node = node.next

                elif node.next == self.tail and self.tail.value == val:
                    self.tail = node
                    self.tail.next = None
                    return
                elif node.next.value == val:
                    node.next = node.next.next
                    node.next.prev = node
                else:
                    node = node.next

            if self.tail.value == val:
                self.tail = None

        else:
            while True:
                if node.value == val and node == self.tail and (
                    self.tail == self.head
                ):
                    self.clean()
                    return
                elif node.value == val and node == self.head:
                    self.head = node.next
                    self.head.prev = None
                    if self.head == self.tail:
                        self.tail.prev = None
                    return
                elif node.next.value == val and node.next == self.tail:
                    self.tail = node
                    self.tail.next = None
                    return
                elif node.next.value == val:
                    node.next = node.next.next
                    node.next.prev = node
                    return
                else:
                    node = node.next

    def clean(self):
        self.head = None
        self.tail = None

    def len(self):
        node = self.head
        items_counter = 0
        while node is not None:
            items_counter += 1
            node = node.next
        return items_counter

    def insert(self, afterNode, newNode):
        if afterNode is None and self.len() == 0:
            self.add_in_tail(newNode)
        elif afterNode is None and self.len() > 0:
            self.add_in_tail(newNode)
        elif afterNode is not None:
            node = self.head
            while node != afterNode:
                node = node.next
            if node == self.tail:
                self.add_in_tail(newNode)
            else:
                newNode.next = node.next
                newNode.prev = node
                node.next = newNode

    def add_in_head(self, newNode):
        newNode.next = self.head
        self.head.prev = newNode
        self.head = newNode
        self.head.prev = None
