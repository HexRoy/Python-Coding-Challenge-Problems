# Problem
# =====================================================================================================================
# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
#
# Return the running sum of nums.
#
#
#
# Example 1:
#
# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
# Example 2:
#
# Input: nums = [1,1,1,1,1]
# Output: [1,2,3,4,5]
# Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
# Example 3:
#
# Input: nums = [3,1,2,10,1]
# Output: [3,4,6,16,17]
#
#
# Constraints:
#
# 1 <= nums.length <= 1000
# -10^6 <= nums[i] <= 10^6


# Solution
# ====================================================================================================================
# Original Solution ~ 50ms
class Solution:
    def runningSum(self, nums):
        if not nums:
            return
        if len(nums) == 1:
            return nums
        running_sum = []
        for i in range(len(nums)):
            running_sum.append(sum(nums[0:i+1]))
        return running_sum

# V2 ~ 32ms
# Storing the current sum values cuts down on runtime
class Solution:
    def runningSum(self, nums):
        running_sum = []
        current = 0
        for i in range(len(nums)):
            current += nums[i]
            running_sum.append(current)
        return running_sum


# Input
# =====================================================================================================================
test = Solution()
print(test.runningSum([1, 2, 3, 4]))
print(test.runningSum([1, 1, 1, 1, 1]))
print(test.runningSum([3, 1, 2, 10, 1]))
