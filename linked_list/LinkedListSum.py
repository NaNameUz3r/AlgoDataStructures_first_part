from linked_list import Node, LinkedList


def linked_list_sum(first_list, second_list):

    if first_list.len() == second_list.len():
        summed_list = LinkedList()

        first_list_node = first_list.head
        second_list_node = second_list.head

        while first_list_node is not None:
            node_values_sum = first_list_node.value + second_list_node.value
            summed_list.add_in_tail(Node(node_values_sum))
            first_list_node = first_list_node.next
            second_list_node = second_list_node.next

        return summed_list
