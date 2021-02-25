# Problem
# =====================================================================================================================
# Given a sorted array arr of distinct integers, return the lowest index i for which arr[i] == i.
# Return null if there is no such index.

# For example, given the array [-5, -3, 2, 3], return 2 since arr[2] == 2.
# Even though arr[3] == 3, we return 2 since it's the lowest index.


# Solution
# =====================================================================================================================
def find_i_equal_to_array_i(n):
    """
    find_i_equal_to_array_i: Finds the index of an array where i == array[i]
    :param n: (List(Ints)) List containing distinct values
    :return: (Int) Where i == array[i]
    """
    for i in range(len(n)):
        if i == n[i]:
            return i
    return None


# Input
# =====================================================================================================================
print(find_i_equal_to_array_i([-5, -3, 2, 3]))