# Problem
# =====================================================================================================================
# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
#
# Follow-up: Could you solve the problem in linear time and in O(1) space?
#
#
#
# Example 1:
#
# Input: nums = [3,2,3]
# Output: [3]
# Example 2:
#
# Input: nums = [1]
# Output: [1]
# Example 3:
#
# Input: nums = [1,2]
# Output: [1,2]
#
#
# Constraints:
#
# 1 <= nums.length <= 5 * 104
# -109 <= nums[i] <= 109

# Solution
# ====================================================================================================================

# Solution ~ 484 ms,
class Solution:
    def majorityElement(self, nums):
        element_frequency = {}
        result = []

        for number in nums:
            if number not in element_frequency:
                element_frequency[number] = 1
            else:
                element_frequency[number] += 1

            if element_frequency[number] > len(nums) / 3 and number not in result:
                result.append(number)
        return result


# Input
# =====================================================================================================================
test = Solution()
print(test.majorityElement([3, 2, 3]))
