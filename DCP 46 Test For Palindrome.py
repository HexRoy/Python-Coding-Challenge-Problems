# Problem
# =====================================================================================================================
# Given a string which we can delete at most k, return whether you can make a palindrome.
# For example, given 'waterrfetawx' and a k of 2, you could delete f and x to get 'waterretaw'.


# Solution
# =====================================================================================================================
from itertools import combinations


def remove_at_least_k(n, k):
    """
    remove_at_least_k: Finds combinations of n, removing up to k letters
    :param n: (String) String that we are testing to see if there is a possible palindrome
    :param k: (Int) Number of letters we are able to remove to test for palindrome
    :return: (True + Palindrome / False)
    """
    if k == 0:
        return is_palindrome(n)
    for i in range(k):
        possible_palindromes = combinations(n, (len(n)-(i+1)))
        for palindrome in possible_palindromes:
            if is_palindrome(palindrome):
                return True, palindrome
    return False


def is_palindrome(n):
    """
    is_palindrome: Checks to see if the input is a palindrome
    :param n: (String) Word we are checking
    :return: (True/False)
    """
    if n[::-1] == n:
        return True
    return False


# Input
# =====================================================================================================================
print(remove_at_least_k('waterrfetawx', 2))     # True
print(remove_at_least_k('waterrfetawx', 1))     # False
print(remove_at_least_k('xyyx', 2))             # True
