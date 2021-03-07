# Problem
# =====================================================================================================================
# Given a binary tree and an integer k, return whether there exists a root-to-leaf path that sums up to k.
# For example, given k = 18 and the following binary tree:
#     8
#    / \
#   4   13
#  / \   \
# 2   6   19
# Return True since the path 8 -> 4 -> 6 sums to 18.


# Solution
# =====================================================================================================================
# Basic Node Class
class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Basic Binary Tree Class
class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)


def root_to_leaf(root, total, n):
    """
    root_to_leaf: Returns True if there is a root to leaf combination of values equal to n
    :param root: (Node) The root of the binary tree
    :param total: (int) The current value of the node path
    :param n: (int) The total target value
    :return: (True/False) True if there is a combination equal to n, Else False
    """

    total += root.value

    # If we are at a leaf
    if (root.left is None) and (root.right is None):
        # And we have the target value
        if total == n:
            return True

    # Checks to see if the current node has a left child
    if root.left is not None:
        ans = root_to_leaf(root.left, total, n)
        if ans is True:
            return True

    # Checks to see if the current node has a right child
    if root.right is not None:
        ans = root_to_leaf(root.right, total, n)
        if ans is True:
            return True


# Input
# =====================================================================================================================
# Creating the tree
tree = BinaryTree(8)
tree.root.left = Node(4)
tree.root.right = Node(13)
tree.root.left.left = Node(2)
tree.root.left.right = Node(6)
tree.root.right.right = Node(19)

print(root_to_leaf(tree.root, 0, 18))
