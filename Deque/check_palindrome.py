from deque import Deque


def is_palindrome(string_to_check):
    deque = Deque()
    for item in string_to_check:
        deque.addFront(item)

    while deque.size() > 1:
        if deque.removeFront() != deque.removeTail():
            return False
    return True

