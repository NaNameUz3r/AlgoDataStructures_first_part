from linked_list import LinkedList, Node


class Stack:
    def __init__(self):
        self.stack = LinkedList()

    def size(self):
        return self.stack.len()

    def pop(self):
        if self.size() < 1:
            return None
        else:
            x = self.stack.pop_from_head()
            return x

    def push(self, value):
        self.stack.add_in_head(Node(value))

    def peek(self):
        if self.size() < 1:
            return None
        else:
            return self.stack.head.next.value

