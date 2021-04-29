# Problem
# =====================================================================================================================
# Given an integer number n, return the difference between the product of its digits and the sum of its digits.
#
#
# Example 1:
#
# Input: n = 234
# Output: 15
# Explanation:
# Product of digits = 2 * 3 * 4 = 24
# Sum of digits = 2 + 3 + 4 = 9
# Result = 24 - 9 = 15
# Example 2:
#
# Input: n = 4421
# Output: 21
# Explanation:
# Product of digits = 4 * 4 * 2 * 1 = 32
# Sum of digits = 4 + 4 + 2 + 1 = 11
# Result = 32 - 11 = 21
#
#
# Constraints:
#
# 1 <= n <= 10^5


# Solution
# ====================================================================================================================
import math  # For square root (Distance formula)


# Solution: 28 ms
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        the_product = 1
        the_sum = 0
        for num in str(n):
            the_product *= int(num)
            the_sum += int(num)
        return the_product - the_sum


# Input
# =====================================================================================================================
obj = Solution()
print(obj.subtractProductAndSum(234))

