# Problem
# =====================================================================================================================
# Given a binary tree, return the level of the tree with minimum sum.


# Solution
# ====================================================================================================================
class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


SUM_LIST = []


def find_lowest_level_sum(root, level):
    if root is None:
        return

    SUM_LIST[level][0] += root.value

    find_lowest_level_sum(root.left, level + 1)
    find_lowest_level_sum(root.right, level + 1)


def find_max_levels(root):
    left = 0
    if root.left is not None:
        left = find_max_levels(root.left)

    right = 0
    if root.right is not None:
        right = find_max_levels(root.right)

    if left > right:
        return left + 1
    else:
        return right + 1


def populate_array(max_level):
    for i in range(max_level):
        SUM_LIST.append([0])


# Input
# =====================================================================================================================
tree = Node(1)
tree.left = Node(1)
tree.right = Node(1)
tree.left.left = Node(4)
tree.left.left.left = Node(4)
tree.left.right = Node(4)
tree.left.right.right = Node(4)
tree.right.left = Node(4)
tree.right.right = Node(4)

max_levels = find_max_levels(tree)
print("Max Level: ", max_levels)
populate_array(max_levels)
find_lowest_level_sum(tree, 0)
print("Lowest Sum Level: ", min(SUM_LIST)[0])
