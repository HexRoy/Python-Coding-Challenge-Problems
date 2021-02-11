# Problem
# =====================================================================================================================
# Write a function that takes a natural number as input and returns the number of digits the input has.
# Constraint: don't use any loops.


# Solution
# =====================================================================================================================
def length_of_natural_number(n):
    """
    length_of_natural_number:
    :param n: (int) Natural number
    :return: (int) Length of the natural number's digits
    """
    return len(str(n))


# Input
# =====================================================================================================================
print(length_of_natural_number(1))
print(length_of_natural_number(11))
print(length_of_natural_number(111))
