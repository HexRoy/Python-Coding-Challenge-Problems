# Problem
# =====================================================================================================================
# Given the root of a Binary Search Tree and a target number k,
# return true if there exist two elements in the BST such that their sum is equal to the given target.
#
#
#
# Example 1:
#
#
# Input: root = [5,3,6,2,4,null,7], k = 9
# Output: true
# Example 2:
#
#
# Input: root = [5,3,6,2,4,null,7], k = 28
# Output: false
# Example 3:
#
# Input: root = [2,1,3], k = 4
# Output: true
# Example 4:
#
# Input: root = [2,1,3], k = 1
# Output: false
# Example 5:
#
# Input: root = [2,1,3], k = 3
# Output: true
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [1, 104].
# -104 <= Node.val <= 104
# root is guaranteed to be a valid binary search tree.
# -105 <= k <= 105


# Solution
# ====================================================================================================================

# Solution ~ 192 ms
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from itertools import combinations


class Solution:
    def __init__(self):
        self.all_values = []

    def findTarget(self, root: TreeNode, k: int) -> bool:
        self.get_values(root)
        sums = combinations(self.all_values, 2)
        for current in sums:
            if sum(current) == k:
                return True
        return False

    def get_values(self, root):
        if root:
            self.all_values.append(root.val)
            self.get_values(root.left)
            self.get_values(root.right)
        return


# Input
# =====================================================================================================================
# test = Solution()
# print(test.numJewelsInStones("aA", "aAAbbbb"))
