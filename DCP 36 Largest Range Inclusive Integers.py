# Problem
# =====================================================================================================================
# Given an array of integers, return the largest range, inclusive,
# of integers that are all included in the array.

# For example, given the array [9, 6, 1, 3, 8, 10, 12, 11],
# return (8, 12) since 8, 9, 10, 11, and 12 are all in the array.


# Solution
# =====================================================================================================================
def longest_range(n):
    n.sort()
    lower = None
    upper = None
    max_sequence = 1
    temp = 1

    for i in range(1, len(n)):
        if n[i-1]+1 == n[i]:
            temp += 1
            if temp > max_sequence:
                max_sequence = temp
                upper = n[i]
                lower = n[i-max_sequence + 1]
        else:
            temp = 1
    return lower, upper


# Input
# =====================================================================================================================
print(longest_range([9, 6, 1, 3, 8, 10, 12, 11]))
