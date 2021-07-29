from stack_reversed import Stack


def postfix_calculator(data_string):
    first_stack = Stack()
    second_stack = Stack()

    for item in data_string.split()[::-1]:
        first_stack.push(item)

    while first_stack.size() > 0:
        element = first_stack.pop()
        if element.isdigit():
            second_stack.push(int(element))
        elif element == "=":
            return second_stack.pop()
        elif second_stack.size() >= 2:
            operation = element
            first_digit = second_stack.pop()
            second_digit = second_stack.pop()
            # !!! NEVER USE eval ON SERVERS !!!
            evaluation = eval(f'{first_digit} {operation} {second_digit}')
            second_stack.push(evaluation)

