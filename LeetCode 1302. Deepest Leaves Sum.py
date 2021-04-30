# Problem
# =====================================================================================================================
# Given the root of a binary tree, return the sum of values of its deepest leaves.
#
#
# Example 1:
#
#
# Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
# Output: 15
# Example 2:
#
# Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
# Output: 19
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [1, 104].
# 1 <= Node.val <= 100


# Solution
# ====================================================================================================================

# Solution: 104 ms
class Solution:
    def __init__(self):
        self.result = 0

    def deepestLeavesSum(self, root: TreeNode) -> int:
        self.get_sum_deepest(root, 1, self.get_max_depth(root, 1, 0))
        return self.result

    def get_max_depth(self, root, current, max_depth):
        if not root:
            return max_depth

        if current > max_depth:
            max_depth = current

        highest_left = self.get_max_depth(root.left, current + 1, max_depth)
        highest_right = self.get_max_depth(root.right, current + 1, max_depth)

        return max(highest_left, highest_right)

    def get_sum_deepest(self, root, current, max_depth):
        if not root:
            return

        if current == max_depth:
            self.result += root.val

        self.get_sum_deepest(root.left, current + 1, max_depth)
        self.get_sum_deepest(root.right, current + 1, max_depth)


# Input
# =====================================================================================================================
# obj = Solution()
# print(obj.deepestLeavesSum([1,2,3,4,5,null,6,7,null,null,null,null,8]))
