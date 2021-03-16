# Problem
# =====================================================================================================================
# Given a list of strictly positive integers,
# partition the list into 3 contiguous partitions which each sum up to the same value. If not possible, return null.
# For example, given the following list:
# [3, 5, 8, 0, 8]
# Return the following 3 partitions:
# [[3, 5],
#  [8, 0],
#  [8]]
# Which each add up to 8.


# Solution
# =====================================================================================================================
def three_equal_partitions(n):
    """
    three_equal_partitions: Determines if an array of positive integers can be broken down into 3 equal summing lists
    :param n: (List(Ints)) List of positive integers
    :return: (List(List(Ints))) A list Containing three lists of integers
    """
    # Nested loop to select where the list is partitioned
    for i in range(len(n)):
        result = [[], [], []]
        for j in range(i, len(n)):
            result[0] = n[0:i]
            result[1] = n[i:j]
            result[2] = n[j:len(n)]
        if (sum(result[0]) == sum(result[1])) and (sum(result[1]) == sum(result[2])):
            return result
    return None


# Input
# =====================================================================================================================
print(three_equal_partitions([3, 5, 8, 0, 8]))




