# Problem
# =====================================================================================================================
# Given two integers num1 and num2, return the sum of the two integers.
# Example 1:
#
# Input: num1 = 12, num2 = 5
# Output: 17
# Explanation: num1 is 12, num2 is 5, and their sum is 12 + 5 = 17, so 17 is returned.
# Example 2:
#
# Input: num1 = -10, num2 = 4
# Output: -6
# Explanation: num1 + num2 = -6, so -6 is returned.

# Solution
# ====================================================================================================================
# Runtime: 34 ms, faster than 69.78% of Python3 online submissions for Add Two Integers.
# Memory Usage: 13.8 MB, less than 51.71% of Python3 online submissions for Add Two Integers.
class Solution:
    def sum(self, num1, num2):
        return sum([num1, num2])

# Input
# =====================================================================================================================
obj = Solution()
print(obj.sum(1, 1))

