# Problem
# =====================================================================================================================
# Given a string, generate all possible subsequences of the string.
# For example, given the string xyz, return an array or set with the following strings:
#
# x
# y
# z
# xy
# xz
# yz
# xyz
# Note that zx is not a valid subsequence since it is not in the order of the given string.


# Solution
# =====================================================================================================================
from itertools import combinations


def all_substring(n):
    """
    all_substring: Finds all substrings of a given string
    :param n: (string) Original string
    :return: (list) All possible substring
    """
    substrings = []
    for i in range(len(n)):
        temp_substring = combinations(n, i+1)
        for sub in temp_substring:
            substrings.append(sub)
    return substrings


# Input
# =====================================================================================================================
print(all_substring('xyz'))
