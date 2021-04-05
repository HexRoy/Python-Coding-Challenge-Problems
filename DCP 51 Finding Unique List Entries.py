# Problem
# =====================================================================================================================
# Given an array of integers in which two elements appear exactly once and all other elements appear exactly twice,
# find the two elements that appear only once.

# For example, given the array [2, 4, 6, 8, 10, 2, 6, 10], return 4 and 8. The order does not matter.


# Solution
# ====================================================================================================================
def find_single_entries(n):
    """
    find_single_entries: Finds the two elements in a list that only appear once
    :param n: (List(Ints)) - All numbers are repeated once, excluding the two unique values
    :return: (Int) - The two unique values
    """
    single_nums = []
    for num in n:
        if n.count(num) == 1:
            single_nums.append(num)
    return single_nums


# Input
# =====================================================================================================================
print(find_single_entries([2, 4, 6, 8, 10, 2, 6, 10]))
