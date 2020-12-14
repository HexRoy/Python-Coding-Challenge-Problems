# Question
# ===================================================================================================================
# Implement an efficient string matching algorithm.
# That is, given a string of length N and a pattern of length k,

# Bonus:
# write a program that searches for the pattern in the string with less than O(N * k) worst-case time complexity.

# If the pattern is found, return the start index of its location. If not, return False.


# Solution
# ===================================================================================================================
def find_pattern(String, Pattern):
    """
    find_pattern: Finds a pattern in a given string
    :param String: Input string to be searched through
    :param Pattern: The pattern that will be searched for in String
    :return: If the pattern is found, return the start index of its location. If not, return False.
    """

    for i in range(len(String) - (len(Pattern) - 1)):
        if String[i:i+len(Pattern)] == Pattern:
            return print('Found at index:', i)
    return False


# Tests
# ===================================================================================================================
find_pattern('12345', '123')
find_pattern('This is my string', 'my string')
find_pattern('This is my string', 'can not find')
