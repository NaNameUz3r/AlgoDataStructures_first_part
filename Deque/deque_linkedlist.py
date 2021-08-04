from linked_list import LinkedList, Node


class Deque:
    def __init__(self):
        self.deque = LinkedList()

    def addFront(self, item):
        self.deque.add_in_head(Node(item))

    def addTail(self, item):
        self.deque.add_in_tail(Node(item))

    def removeFront(self):
        if self.size() > 0:
            return self.deque.pop_from_head()
        else:
            return None

    def removeTail(self):
        if self.size() > 0:
            return self.deque.pop_from_tail()
        else:
            return None

    def size(self):
        return self.deque.len()
