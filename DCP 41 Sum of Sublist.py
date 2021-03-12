# Problem
# =====================================================================================================================
# Given a list of numbers L,
# implement a method sum(i, j) which returns the sum from the sublist L[i:j] (including i, excluding j).
# For example, given L = [1, 2, 3, 4, 5], sum(1, 3) should return sum([2, 3]), which is 5.


# Solution
# =====================================================================================================================
def sum_sublist(l, index):
    """
    sum_sublist
    :param l: (List(Ints)) List of integers to be summed
    :param index: (Tuple(Ints)) Index for what to take the sum of
    :return: sum(list) Sum of the partial list
    """
    return sum(l[index[0]:index[1]])


# Input
# =====================================================================================================================
print(sum_sublist([1, 2, 3, 4, 5], (1, 3)))
