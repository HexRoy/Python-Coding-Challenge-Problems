# Problem
# =====================================================================================================================
# Given a linked list and an integer k, remove the k-th node from the end of the list 
# k is guaranteed to be smaller than the length of the list.
# Do this in one pass.


# Solution
# =====================================================================================================================
# Node Class
class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


# Linked List Class
class LinkedList(object):
    def __init__(self):
        self.head = None

    # To handle printing linked list
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.value)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)


def pop_last_node(node):
    """
    pop_last_node: Takes a node and if the next node is the last, point the second to last node to None
    :param node: Node
    :return: The head of the linked list
    """
    if node.next.next is None:
        node.next = None
    else:
        pop_last_node(node.next)


# Input
# =====================================================================================================================
linked = LinkedList()
first_node = Node("a")
second_node = Node("b")
third_node = Node("c")
linked.head = first_node

first_node.next = second_node
second_node.next = third_node
print(linked)
pop_last_node(first_node)
print(linked)