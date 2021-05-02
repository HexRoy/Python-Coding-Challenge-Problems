# Problem
# =====================================================================================================================
# You have n  tiles, where each tile has one letter tiles[i] printed on it.
#
# Return the number of possible non-empty sequences of letters you can make using the letters printed on those tiles.
#
#
#
# Example 1:
#
# Input: tiles = "AAB"
# Output: 8
# Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".
# Example 2:
#
# Input: tiles = "AAABBC"
# Output: 188
# Example 3:
#
# Input: tiles = "V"
# Output: 1
#
#
# Constraints:
#
# 1 <= tiles.length <= 7
# tiles consists of uppercase English letters.

# Solution
# ====================================================================================================================
# Original Solution ~ 7044 ms
from itertools import permutations

class Solution:
    def numTilePossibilities(self, tiles):
        result = []
        for i in range(0, len(tiles)):
            combos = permutations(tiles, i + 1)
            for combo in combos:
                if combo not in result:
                    result.append(combo)

        return len(result)


# Input
# =====================================================================================================================
test = Solution()
print(test.numTilePossibilities("AAB"))
