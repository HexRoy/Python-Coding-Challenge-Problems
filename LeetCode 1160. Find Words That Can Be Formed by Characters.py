# Problem
# =====================================================================================================================
# You are given an array of strings words and a string chars.
#
# A string is good if it can be formed by characters from chars (each character can only be used once).
#
# Return the sum of lengths of all good strings in words.
#
#
#
# Example 1:
#
# Input: words = ["cat","bt","hat","tree"], chars = "atach"
# Output: 6
# Explanation:
# The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
# Example 2:
#
# Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
# Output: 10
# Explanation:
# The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.
#
#
# Note:
#
# 1 <= words.length <= 1000
# 1 <= words[i].length, chars.length <= 100
# All strings contain lowercase English letters only.


# Solution
# ====================================================================================================================

# 216 ms
class Solution:
    def countCharacters(self, words, chars):
        result = ""
        usable_chars = self.map_to_dict(chars)
        for word in words:
            used_chars = self.map_to_dict(word)
            valid = True
            for char in used_chars:

                if char not in usable_chars:
                    valid = False
                    break
                if used_chars[char] > usable_chars[char]:
                    valid = False
            if valid:
                result += word

        print(result)
        return len(result)

    def map_to_dict(self, word):
        result = {}

        for char in word:
            if char not in result:
                result[char] = 1
            else:
                result[char] += 1
        return result


# Input
# =====================================================================================================================
obj = Solution()
print(obj.countCharacters(["cat", "bt", "hat", "tree"], "atach"))

