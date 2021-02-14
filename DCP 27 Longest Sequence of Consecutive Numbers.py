# Problem
# =====================================================================================================================
# Given a list of integers L,
# find the maximum length of a sequence of consecutive numbers that can be formed using elements from L.

# For example, given L = [5, 2, 99, 3, 4, 1, 100],
# return 5 as we can build a sequence [1, 2, 3, 4, 5] which has length 5.


# Solution
# =====================================================================================================================
def longest_sequence(n):
    n.sort()
    max_sequence = 1
    temp = 1

    for i in range(1, len(n)):
        if n[i-1]+1 == n[i]:
            temp += 1
            if temp > max_sequence:
                max_sequence = temp
        else:
            temp = 1
    return max_sequence


# Input
# =====================================================================================================================
print(longest_sequence([5, 2, 99, 3, 4, 1, 100]))
