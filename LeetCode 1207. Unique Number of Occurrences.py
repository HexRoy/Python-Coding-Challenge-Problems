# Problem
# =====================================================================================================================
# Given an array of integers arr,
# write a function that returns true if and only if the number of occurrences of each value in the array is unique.
#
#
#
# Example 1:
#
# Input: arr = [1,2,2,1,1,3]
# Output: true
# Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
# Example 2:
#
# Input: arr = [1,2]
# Output: false
# Example 3:
#
# Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
# Output: true
#
#
# Constraints:
#
# 1 <= arr.length <= 1000
# -1000 <= arr[i] <= 1000


# Solution Python
# ====================================================================================================================
# Original Solution ~ 52 ms
class Solution:
    def uniqueOccurrences(self, arr):
        count = {}
        for i in range(len(arr)):
            if arr[i] not in count:
                if arr.count(arr[i]) in count.values():
                    return False
                else:
                    count[arr[i]] = arr.count(arr[i])
        return True


# Input
# =====================================================================================================================
test = Solution()
print(test.uniqueOccurrences([1,2,2,1,1,3]))
