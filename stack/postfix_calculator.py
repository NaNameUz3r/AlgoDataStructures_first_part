from stack_reversed import Stack
import operator


def postfix_calculator(data_string):
    first_stack = Stack()
    second_stack = Stack()

    operations = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }

    for item in data_string.split()[::-1]:
        first_stack.push(item)

    while first_stack.size() > 0:
        element = first_stack.pop()
        if element.isdigit():
            second_stack.push(int(element))
        elif element == "=":
            return second_stack.pop()
        elif second_stack.size() >= 2:
            first_digit = second_stack.pop()
            second_digit = second_stack.pop()
            evaluation = operations[element](first_digit, second_digit)
            second_stack.push(evaluation)
