# Problem
# =====================================================================================================================
# We are given two strings, A and B.
#
# A shift on A consists of taking string A and moving the leftmost character to the rightmost position. For example,
# if A = 'abcde', then it will be 'bcdea' after one shift on A.
# Return True if and only if A can become B after some number of shifts on A.
#
# Example 1:
# Input: A = 'abcde', B = 'cdeab'
# Output: true
#
# Example 2:
# Input: A = 'abcde', B = 'abced'
# Output: false
# Note:
#
# A and B will have length at most 100.

# Solution
# ====================================================================================================================

# Solution ~ 24 ms
class Solution:
    def rotateString(self, A, B) -> bool:
        # Check for same len strings
        if len(A) != len(B):
            return False

        if A == B:
            return True

        str_len = len(A)

        for i in range(str_len):
            if B[i] == A[0]:
                test_str = B[i:] + B[:i]
                if A == test_str:
                    return True

        return False


# Input
# =====================================================================================================================
test = Solution()
print(test.rotateString("abcde", "cdeab"))
