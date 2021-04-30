# Problem
# =====================================================================================================================
# For two strings s and t, we say "t divides s" if and only if s = t + ... + t
# (t concatenated with itself 1 or more times)
#
# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.
#
#
#
# Example 1:
#
# Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"
# Example 2:
#
# Input: str1 = "ABABAB", str2 = "ABAB"
# Output: "AB"
# Example 3:
#
# Input: str1 = "LEET", str2 = "CODE"
# Output: ""
# Example 4:
#
# Input: str1 = "ABCDEF", str2 = "ABC"
# Output: ""
#
#
# Constraints:
#
# 1 <= str1.length <= 1000
# 1 <= str2.length <= 1000
# str1 and str2 consist of English uppercase letters.


# Solution
# ====================================================================================================================

# Solution ~ 192 ms
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        string1_repeats = self.get_repeats(str1)
        string2_repeats = self.get_repeats(str2)
        longest_repeat = self.get_longest_repeat(string1_repeats, string2_repeats)
        return longest_repeat

    def get_repeats(self, string):
        repeats = []
        current = ''
        for i in range(len(string)):
            current += string[i]

            mutiplier = len(string) / len(current)
            if mutiplier.is_integer():
                if current * int(mutiplier) == string:
                    repeats.append(current)
        return repeats

    def get_longest_repeat(self, list1, list2):

        list1.reverse()

        for word in list1:
            if word in list2:
                return word
        return ""


# Input
# =====================================================================================================================
test = Solution()
print(test.gcdOfStrings("ABCABC", "ABC"))
