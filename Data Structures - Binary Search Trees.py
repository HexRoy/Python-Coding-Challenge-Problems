# Simple Binary Search Tree Implementation
class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return # node already exist

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def find_min(self):
        if self.left:
            return self.left.find_min()
        else:
            return self.data

    def find_max(self):
        if self.right:
            return self.right.find_max()
        else:
            return self.data

    def calculate_sum(self):
        total = 0
        if self.left:
            total += self.left.calculate_sum()
        total += self.data
        if self.right:
            total += self.right.calculate_sum()
        return total

    def post_order_traversal(self):
        element = []
        if self.left:
            element += self.left.post_order_traversal()

        if self.right:
            element += self.right.post_order_traversal()

        element.append(self.data)

        return element

    def pre_order_traversal(self):
        elements = [self.data]
        if self.left:
            elements += self.left.in_order_traversal()

        if self.right:
            elements += self.right.in_order_traversal()
        return elements

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            # Setting the max value as the target

            max_val = self.left.find_max()
            self.data = max_val
            self.left = self.left.delete(max_val)


            # Setting the min value as the target

            # min_val = self.right.find_min()
            # self.data = min_val
            # self.right = self.right.delete(min_val)

        return self

def build_tree(elements):
    print("Building tree with these elements:",elements)
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == '__main__':
    countries = ["India","Pakistan","Germany", "USA","China","India","UK","USA"]
    country_tree = build_tree(countries)

    print("UK is in the list? ", country_tree.search("UK"))
    print("Sweden is in the list? ", country_tree.search("Sweden"))

    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    print("In order traversal gives this sorted list:",numbers_tree.in_order_traversal())

    print("min", numbers_tree.find_min())
    print("max", numbers_tree.find_max())
    print("sum", numbers_tree.calculate_sum())
    print("Post order traversal", numbers_tree.post_order_traversal())
    print("Pre order traversal", numbers_tree.pre_order_traversal())
    print("Deleting 20", numbers_tree.delete(20).in_order_traversal())

# Binary Tree Part 1 Exercise
# Add following methods to BinarySearchTreeNode class created in main video tutorial
#
# 1. find_min(): finds minimum element in entire binary tree
# 2. find_max(): finds maximum element in entire binary tree
# 3. calculate_sum(): calcualtes sum of all elements
# 4. post_order_traversal(): performs post order traversal of a binary tree
# 5. pre_order_traversal(): perofrms pre order traversal of a binary tree
# Solution

# Binary Tree Part 2 Exercise
# Modify delete method in class BinarySearchTreeNode class to use min element from left subtree.
# You will remove lines marked with ---> and use max value from left subtree
#
#     def delete(self, val):
#         if val < self.data:
#             if self.left:
#                 self.left = self.left.delete(val)
#         elif val > self.data:
#             if self.right:
#                 self.right = self.right.delete(val)
#         else:
#             if self.left is None and self.right is None:
#                 return None
#             elif self.left is None:
#                 return self.right
#             elif self.right is None:
#                 return self.right
#
#           --->  min_val = self.right.find_min()
#           --->  self.data = min_val
#           --->  self.right = self.right.delete(min_val)
