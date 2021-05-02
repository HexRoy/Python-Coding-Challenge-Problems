# Problem
# =====================================================================================================================
# Given two strings a and b, return true if you can swap two letters in a so the result is equal to b, otherwise,
# return false.
#
# Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the
# characters at a[i] and a[j].
#
# For example, swapping at indices 0 and 2 in "abcd" results in "cbad".
#
#
# Example 1:
#
# Input: a = "ab", b = "ba"
# Output: true
# Explanation: You can swap a[0] = 'a' and a[1] = 'b' to get "ba", which is equal to b.
# Example 2:
#
# Input: a = "ab", b = "ab"
# Output: false
# Explanation: The only letters you can swap are a[0] = 'a' and a[1] = 'b', which results in "ba" != b.
# Example 3:
#
# Input: a = "aa", b = "aa"
# Output: true
# Explanation: You can swap a[0] = 'a' and a[1] = 'a' to get "aa", which is equal to b.
# Example 4:
#
# Input: a = "aaaaaaabc", b = "aaaaaaacb"
# Output: true
#
#
# Constraints:
#
# 1 <= a.length, b.length <= 2 * 104
# a and b consist of lowercase letters.


# Solution
# ====================================================================================================================

# Solution ~ 36 ms,
class Solution:
    def buddyStrings(self, a: str, b: str) -> bool:
        if len(a) != len(b):
            return False

        index = []
        double_letters = False

        for i in range(len(a)):
            if a[i] != b[i]:
                index.append(i)
            if double_letters == False:
                if a.count(a[i]) >= 2:
                    double_letters = True

        if len(index) == 2:
            temp = list(a)
            temp[index[0]] = a[index[1]]
            temp[index[1]] = a[index[0]]

            if "".join(temp) == b:
                return True
        elif len(index) == 0 and double_letters == True:
            return True

        else:
            return False

# Input
# =====================================================================================================================
test = Solution()
print(test.buddyStrings("ab", "ba"))
