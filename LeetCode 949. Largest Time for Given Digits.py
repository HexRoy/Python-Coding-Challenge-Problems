# Problem
# =====================================================================================================================
# You are given an array items, where each items[i] = [typei, colori, namei] describes the type, color,
# and name of the ith item. You are also given a rule represented by two strings, ruleKey and ruleValue.
#
# The ith item is said to match the rule if one of the following is true:
#
# ruleKey == "type" and ruleValue == typei.
# ruleKey == "color" and ruleValue == colori.
# ruleKey == "name" and ruleValue == namei.
# Return the number of items that match the given rule.
#
#
#
# Example 1:
#
# Input: items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]],
# ruleKey = "color", ruleValue = "silver"Given an array arr of 4 digits, find the latest 24-hour time
# that can be made using each digit exactly once.
#
# 24-hour times are formatted as "HH:MM", where HH is between 00 and 23, and MM is between 00 and 59.
# The earliest 24-hour time is 00:00, and the latest is 23:59.
#
# Return the latest 24-hour time in "HH:MM" format.  If no valid time can be made, return an empty string.
#
#
#
# Example 1:
#
# Input: arr = [1,2,3,4]
# Output: "23:41"
# Explanation:
# The valid 24-hour times are "12:34", "12:43", "13:24", "13:42", "14:23", "14:32", "21:34", "21:43", "23:14",
# and "23:41". Of these times, "23:41" is the latest.


# Example 2:
#
# Input: arr = [5,5,5,5]
# Output: ""
# Explanation: There are no valid 24-hour times as "55:55" is not valid.
# Example 3:
#
# Input: arr = [0,0,0,0]
# Output: "00:00"
# Example 4:
#
# Input: arr = [0,0,1,0]
# Output: "10:00"
#
#
# Constraints:
#
# arr.length == 4
# 0 <= arr[i] <= 9


# Solution
# ====================================================================================================================

# Solution: 28 ms
from itertools import permutations


class Solution:
    def largestTimeFromDigits(self, arr):
        all_times = permutations(arr)
        valid_times = []
        for time in all_times:
            if time[0] == 2:
                if time[1] < 4:
                    if time[2] < 6:
                        valid_times.append(time)

            if time[0] == 1:
                if time[1] < 10:
                    if time[2] < 6:
                        valid_times.append(time)

            if time[0] == 0:
                if time[1] < 10:
                    if time[2] < 6:
                        valid_times.append(time)
        if not valid_times:
            return ""

        temp = list(sorted(valid_times)[len(valid_times) - 1])
        largest_time = str(temp[0]) + str(temp[1]) + ":" + str(temp[2]) + str(temp[3])

        return largest_time


# Input
# =====================================================================================================================
obj = Solution()
print(obj.largestTimeFromDigits([1, 2, 3, 4]))
