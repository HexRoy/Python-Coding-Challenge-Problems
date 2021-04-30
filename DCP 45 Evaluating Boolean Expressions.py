# Problem
# =====================================================================================================================
# You are presented with an array representing a Boolean expression. The elements are of two kinds:
# •	T and F, representing the values True and False.
# •	&, |, and ^, representing the bitwise operators for AND, OR, and XOR.
# Determine the number of ways to group the array elements using parentheses so that
# the entire expression evaluates to True.

# For example, suppose the input is ['F', '|', 'T', '&', 'T']. In this case,
# there are two acceptable groupings: (F | T) & T and F | (T & T).

# Solution
# =====================================================================================================================
from itertools import combinations


def is_boolean_true(expression):
    """
    is_boolean_true:
    :param expression: (List(String)) Contains the components of a boolean expression
                        Possible strings: T - True, F - False, & - AND, | - OR, ^ - XOR
    :return: (List(List(String))) List containing the evaluation of the expression that are True
    """
    test = combinations(expression, 2)
    for combo in test:
        print(combo)
    #for partial in expression:



# Input
# =====================================================================================================================
print(is_boolean_true(['F', '|', 'T', '&', 'T']))



