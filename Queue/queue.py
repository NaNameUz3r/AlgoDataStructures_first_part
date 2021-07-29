from linked_list import LinkedList, Node


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
