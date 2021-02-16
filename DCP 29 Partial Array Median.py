# Problem
# =====================================================================================================================
# Given an array of numbers arr and a window of size k,
# print out the median of each window of size k starting from the left and moving right by one position each time.
# For example, given the following array and k = 3:
# [-1, 5, 13, 8, 2, 3, 3, 1]
# Your function should print out the following:
# 5 <- median of [-1, 5, 13]
# 8 <- median of [5, 13, 8]
# 8 <- median of [13, 8, 2]
# 3 <- median of [8, 2, 3]
# 3 <- median of [2, 3, 3]
# 3 <- median of [3, 3, 1]
# Recall that the median of an even-sized list is the average of the two middle numbers.


# Solution
# =====================================================================================================================
from statistics import  median


def partial_median(k, n):
    """
    partial_median: Find the median of size k along the array n
    :param k: (int) The amount of numbers to take the median of
    :param n: (Array(int)) Numbers of which to find the median of
    :return: None, Prints out the medians
    """
    # K can not be greater than length of the array
    if k > len(n):
        exit(1)

    for i in range(k, len(n)+1):
        current_median = median(n[i-k:i])
        print(current_median, '<- median of', n[i-k:i])


# Input
# =====================================================================================================================
partial_median(3, [-1, 5, 13, 8, 2, 3, 3, 1])
