# Problem
# =====================================================================================================================
# A pangram is a sentence where every letter of the English alphabet appears at least once.
#
# Given a string sentence containing only lowercase English letters, return true if sentence is a pangram,
# or false otherwise.
#
#
#
# Example 1:
#
# Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
# Output: true
# Explanation: sentence contains at least one of every letter of the English alphabet.
# Example 2:
#
# Input: sentence = "leetcode"
# Output: false
#
#
# Constraints:
#
# 1 <= sentence.length <= 1000
# sentence consists of lowercase English letters.


# Solution
# ====================================================================================================================
# Solution ~ 24 ms
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alpha_dict = {
            'a': False,
            'b': False,
            'c': False,
            'd': False,
            'e': False,
            'f': False,
            'g': False,
            'h': False,
            'i': False,
            'j': False,
            'k': False,
            'l': False,
            'm': False,
            'n': False,
            'o': False,
            'p': False,
            'q': False,
            'r': False,
            's': False,
            't': False,
            'u': False,
            'v': False,
            'w': False,
            'x': False,
            'y': False,
            'z': False
        }

        for letter in sentence:
            if alpha_dict[letter] is False:
                alpha_dict[letter] = True

        if all(isInWord is True for isInWord in alpha_dict.values()):
            return True
        return False


# Input
# =====================================================================================================================
obj = Solution()
print(obj.checkIfPangram("thequickbrownfoxjumpsoverthelazydog"))

