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

    def compare(self, v1, v2):
        if v1 < v2:
            return -1
        elif v1 == v2:
            return 0
        elif v1 > v2:
            return +1

    def add(self, value):
        node = self.head
        new_node = Node(value)


        if self.__ascending:
            found_flag = False
            while node is not None and not found_flag:
                if node.value > value


    def find(self, val):
        return None # здесь будет ваш код

    def delete(self, val):
        pass # здесь будет ваш код

    def clean(self, asc=True):
        self.__ascending = asc
        pass # здесь будет ваш код

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
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1, v2):
        # переопределённая версия для строк
        return 0
