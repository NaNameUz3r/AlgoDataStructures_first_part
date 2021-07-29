class Queue:
    def __init__(self):
        self.queue = LinkedList()

    def enqueue(self, item):
        self.queue.add_in_tail(Node(item))

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop_from_head()
        else:
            return None

    def size(self):
        return self.queue.len()


class Node:
    def __init__(self, v, dummy=False):
        self.value = v
        self.prev = None
        self.next = None
        self.dummy = False

        if dummy:
            self.dummy = True

    def get_next(self):
        if not self.next.dummy:
            return self.next
        else:
            return None

    def get_prev(self):
        if not self.prev.dummy:
            return self.prev
        else:
            return None


class LinkedList:
    def __init__(self):
        self.head = Node(None, dummy=True)
        self.tail = Node(None, dummy=True)
        self.head.next = self.tail
        self.tail.prev = self.head

    def print_all_nodes(self):
        node = self.head.get_next()
        while node is not None:
            print(node.value)
            node = node.get_next()

    def add_in_tail(self, new_node):
        if self.head.next is None:
            self.head.next = new_node
        else:
            self.tail.prev.next = new_node
            new_node.next = self.tail
            new_node.prev = self.tail.prev
            self.tail.prev = new_node

    def add_in_head(self, new_node):
        if self.head.get_next() is None:
            self.head.next = new_node
            new_node.prev = self.head
            new_node.next = self.tail
            self.tail.prev = new_node
        else:
            new_node.next = self.head.get_next()
            self.head.get_next().prev = new_node
            self.head.next = new_node
            new_node.prev = self.head

    def pop_from_head(self):
        node = self.head.get_next()
        node_value = node.value
        if self.len() > 1:
            self.head.next = node.next
            node.get_next().prev = self.head
        else:
            self.clean()
        return node_value

    def find(self, val):
        node = self.head.get_next()
        while node is not None:
            if node.value == val:
                return node
            node = node.get_next()
        return None

    def find_all(self, val):
        found_nodes = []
        node = self.head.get_next()
        while node is not None:
            if node.value == val:
                found_nodes.append(node)
            node = node.get_next()

        return found_nodes

    def len(self):
        node = self.head.get_next()
        length = 0
        while node is not None:
            length += 1
            node = node.get_next()
        return length

    def clean(self):
        self.head = Node(None, dummy=True)
        self.tail = Node(None, dummy=True)
        self.head.next = self.tail
        self.tail.prev = self.head

    def delete(self, val, all=False):
        node = self.head.get_next()

        while node is not None:
            if node.value == val and self.len() == 1:
                self.clean()
                if not all:
                    return
            elif node.value == val:
                node.get_prev().next = node.get_next()
                node.get_next().prev = node.get_prev()
                if not all:
                    return
            node = node.get_next()

    def insert(self, after_node, new_node):
        node = self.head.get_next()
        while node != after_node:
            node = node.get_next()
        if node == after_node:
            node.get_next().prev = new_node
            new_node.next = node.get_next()
            new_node.prev = node
            node.next = new_node
