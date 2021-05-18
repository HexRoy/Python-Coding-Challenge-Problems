# Problem
# =====================================================================================================================
# Given an integer array nums, return an array answer such that answer[i]
# is equal to the product of all the elements of nums except nums[i].
#
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
#
# You must write an algorithm that runs in O(n) time and without using the division operation.
#
#
#
# Example 1:
#
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:
#
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
#
#
# Constraints:
#
# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
#
#
# Follow up: Can you solve the problem in O(1) extra space complexity?
# (The output array does not count as extra space for space complexity analysis.)


# Solution
# ====================================================================================================================
# 224 ms
class Solution:
    def productExceptSelf(self, nums):
        # Slow solution
        #         answer = []

        #         for i in range(len(nums)):
        #             temp = nums[:i] + nums[i+1:]
        #             prod = 1
        #             for num in temp:
        #                 prod *= num
        #             answer.append(prod)
        #         return answer

        # Faster Solution
        # Keep track of zero indexes when taking total product.
        # If zero, append all zeros except where the zero index is
        answer = []
        zeros = []
        prod = 1
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros.append(i)
            else:
                prod *= nums[i]

        if len(zeros) == 1:
            answer = [0 for num in nums]
            answer[zeros[0]] = prod
            return answer

        elif len(zeros) > 1:
            answer = [0 for num in nums]
            return answer

        for i in range(len(nums)):
            answer.append(prod // nums[i])
        return answer


# Input
# =====================================================================================================================
obj = Solution()
print(obj.productExceptSelf([1, 2, 3, 4]))

