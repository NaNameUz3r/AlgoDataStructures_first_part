from deque import Deque


def is_palindrome(string_to_check):
    deque = Deque()
    for item in string_to_check:
        deque.addFront(item)

    palindrome_flag = False
    for i in range(deque.size()):
        if deque.removeFront() != string_to_check[i]:
            return palindrome_flag
    else:
        palindrome_flag = True
    return palindrome_flag
