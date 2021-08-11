class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class OrderedList:
    def __init__(self, asc=True):
        self.head = None
        self.tail = None
        self.__ascending = asc

    def print_all_nodes(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next

    def compare(self, v1, v2):
        if v1.value < v2.value:
            return -1
        elif v1.value > v2.value:
            return 1
        else:
            return 0

    def add(self, value):
        node = self.head
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        while node is not None:
            if self.__ascending and self.compare(new_node, node) <= 0 or (
                    not self.__ascending and self.compare(new_node, node) >= 0):
                if node.prev is None:
                    new_node.next = node
                    node.prev = new_node
                    self.head = new_node
                else:
                    node.prev.next = new_node
                    new_node.prev = node.prev
                    new_node.next = node
                    node.prev = new_node
                return
            elif node.next is None:
                node.next = new_node
                new_node.prev = node
                self.tail = new_node
                return
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def delete(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                if node == self.head:
                    self.head = self.head.next
                    if self.head is not None:
                        self.head.prev = None
                if node == self.tail:
                    self.tail = node.prev
                    if self.tail is not None:
                        self.tail.next = None
                if node.prev is not None:
                    node.prev.next = node.next
                if node.next is not None:
                    node.next.prev = node.prev
                return
            else:
                node = node.next
        return 'No {} in list. Nothing is deleted'.format(val)

    def clean(self, asc=True):
        self.__ascending = asc
        self.head = None
        self.tail = None

    def len(self):
        node = self.head
        items_counter = 0
        while node is not None:
            items_counter += 1
            node = node.next
        return items_counter

    def get_all(self):
        r = []
        node = self.head
        while node != None:
            r.append(node)
            node = node.next
        return r


class OrderedStringList(OrderedList):
    def __init__(self, asc):
        self.head = None
        self.tail = None
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1, v2):
        if v1.value.strip() < v2.value.strip():
            return -1
        elif v1.value.strip() > v2.value.strip():
            return 1
        else:
            return 0
