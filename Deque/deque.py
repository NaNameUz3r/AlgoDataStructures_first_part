class Deque:
    def __init__(self):
        self.deque = []

    def addFront(self, item):
        self.deque.insert(0, item)

    def addTail(self, item):
        self.deque.append(item)

    def removeFront(self):
        if self.size() > 0:
            return self.deque.pop(0)
        else:
            return None

    def removeTail(self):
        if self.size() > 0:
            return self.deque.pop(self.size() - 1)
        else:
            return None

    def size(self):
        return len(self.deque)
