# Problem
# =====================================================================================================================
# A permutation can be specified by an array P,
# where P[i] represents the location of the element at i in the permutation.
# For example, [2, 1, 0] represents the permutation where elements at the index 0 and 2 are swapped.

# Given an array and a permutation, apply the permutation to the array.
# For example, given the array ["a", "b", "c"] and the permutation [2, 1, 0], return ["c", "b", "a"].


# Solution
# =====================================================================================================================
def list_permutation(my_list, permutation):
    """
    list_permutation: Swaps elements in a list based on the permutation
    :param my_list: (List(Elements)) List containing anything. Its order will be swapped
    :param permutation: (List(Ints)) List containing the the index of how the elements in my_list should be ordered
    :return: (List(Elements)) An updated list with the permutation applied
    """
    # Checks for invalid input
    if len(my_list) != len(permutation):
        return "Invalid Input"

    # Initializes the solution list
    result = [0] * len(my_list)

    # Applies permutation
    for i in range(len(my_list)):
        result[i] = my_list[permutation[i]]
    return result


# Input
# =====================================================================================================================
print(list_permutation(["a", "b", "c"], [2, 1, 0]))
print(list_permutation(["a", "b", "c"], [2, 1, 0, 2]))


