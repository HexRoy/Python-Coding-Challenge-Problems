# Problem
# =====================================================================================================================
# Given an array of numbers and a number k, determine if there are three entries in the array
# which add up to the specified number k.
# For example, given [20, 303, 3, 4, 25] and k = 49, return true as 20 + 4 + 25 = 49.


# Solution
# =====================================================================================================================
from itertools import combinations


def possible_sum(k, nums):
    """
    possible_sum: Checks to see if you can get k from the sum of three numbers of nums
    :param k: float - the target number
    :param nums: array(float) - contains the numbers that we will take the sum of
    :return: True if possible to create k from the sum of 3 nums, else false
    """
    if len(nums) >= 3:
        comb = combinations(nums, 3)
        for x in comb:
            sum_of_three = sum(x)
            if sum_of_three == k:
                print('Sum found:', x)
                return True
        print('Sum not found')
        return False

    # Not enough elements in input
    print('Invalid input')
    exit(1)


# Input
# =====================================================================================================================
print(possible_sum(49, [20, 303, 3, 4, 25]))
print(possible_sum(49, [20, 303, 3, 4, 2]))
print(possible_sum(49, [20, 303]))
