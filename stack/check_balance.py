from stack_reversed import Stack


def is_balanced(parentheses_string):
    checking_stack = Stack()
    for parenthesis in parentheses_string:
        if parenthesis == "(":
            checking_stack.push('(')
        elif parenthesis == ")" and checking_stack.peek() == "(":
            checking_stack.pop()

    return checking_stack.size() == 0


# print(is_balanced("(())()(())"))
print(is_balanced('()((())()))'))