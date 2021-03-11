# Problem
# =====================================================================================================================
# Given a string, sort it in decreasing order based on the frequency of characters.
# If there are multiple possible solutions, return any of them.
# For example, given the string tweet, return tteew. eettw would also be acceptable.


# Solution
# =====================================================================================================================
def sort_by_letter_frequency(n):
    """
    sort_by_letter_frequency: Takes a string as input and returns a string with the letters grouped and in order of
                                frequency
    :param n: (String) The input string to be sorted
    :return:  (String) The input string but letters are sorted by frequency
    """
    letter_dict = {}
    solution = ''
    for letter in n:
        if letter in letter_dict:
            letter_dict[letter] += 1
        else:
            letter_dict[letter] = 1

    sorted_letter_list = sorted(letter_dict, key=letter_dict.get, reverse=True)

    for letter in sorted_letter_list:
        value = letter_dict[letter]
        for i in range(value):
            solution += letter

    return solution


# Input
# =====================================================================================================================
print(sort_by_letter_frequency('tweet'))
