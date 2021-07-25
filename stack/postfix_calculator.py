from stack_reversed import Stack


def postfix_calculator(data_string):
    first_stack = Stack()
    second_stack = Stack()

    for item in data_string.split()[::-1]:
        first_stack.push(item)

    while first_stack.size() > 0:
        element = first_stack.pop()
        if element == "+":
            print(second_stack.stack)
            addition = second_stack.pop() + second_stack.pop()
            second_stack.push(addition)
        elif element == "*":
            multiple = second_stack.pop() * second_stack.pop()
            second_stack.push(multiple)
        elif element == "=":
            return second_stack.pop()
        else:
            second_stack.push(int(element))
