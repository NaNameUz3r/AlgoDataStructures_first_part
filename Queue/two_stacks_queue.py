from stack import Stack


class TwoStackQueue:
    def __init__(self):
        self.first_stack = Stack()
        self.second_stack = Stack()

    def enqueue(self, item):
        self.first_stack.push(item)

    def dequeue(self):
        if self.second_stack.size() == 0:
            while self.first_stack.size() > 0:
                self.second_stack.push(self.first_stack.pop())

        if self.second_stack.size() > 0:
            return self.second_stack.pop()
        else:
            return None

    def size(self):
        return self.first_stack.size()
