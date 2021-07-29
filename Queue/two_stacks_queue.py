from stack import Stack


class TwoStackQueue:
    def __init__(self):
        self.first_stack = Stack()
        self.second_stack = Stack()

    def enqueue(self, item):

        while self.first_stack.size() > 0:
            self.second_stack.push(self.first_stack.pop())

        self.first_stack.push(item)

        while self.second_stack.size() > 0:
            self.first_stack.push(self.second_stack.pop())

    def dequeue(self):
        if self.size() > 0:
            return self.first_stack.pop()
        else:
            return None

    def size(self):
        return self.first_stack.size()