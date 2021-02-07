# Problem
# =====================================================================================================================
# A girl is walking along an apple orchard with a bag in each hand.
# She likes to pick apples from each tree as she goes along,
# but is meticulous about not putting different kinds of apples in the same bag.

# Given an input describing the types of apples she will pass on her path, in order,
# determine the length of the longest portion of her path that consists of just two types of apple trees.

# For example, given the input [2, 1, 2, 3, 3, 1, 3, 5],
# the longest portion will involve types 1 and 3, with a length of four.


# Solution
# =====================================================================================================================
def longest_two_types(n):
    """
    longest_two_types: Finds the longest subsection of a list of numbers containing only two numbers
    :param n: (list(ints)) - List of numbers each number representing a different apple type
    :return: Longest sublist of only two types of apples
    """

    length = 0
    for j in range(len(n)):
        temp = 0
        apple_one = None
        apple_two = None
        for i in range(j, len(n)):
            if apple_one is None:
                apple_one = n[j]
                temp += 1

            elif n[i] != apple_one and apple_two is None:
                apple_two = n[i]
                temp += 1

            elif n[i] == apple_one or n[i] == apple_two:
                temp += 1

            else:
                if temp > length:
                    length = temp
                break
    return length

# Input
# =====================================================================================================================
print(longest_two_types([2, 1, 2, 3, 3, 1, 3, 5]))
print(longest_two_types([2, 1, 2, 3, 3, 1, 1, 3, 5]))
