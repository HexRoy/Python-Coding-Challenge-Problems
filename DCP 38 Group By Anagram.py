# Problem
# =====================================================================================================================
# Given an array of strings, group anagrams together.
# For example, given the following array:
# ['eat', 'ate', 'apt', 'pat', 'tea', 'now']
# Return:
# [['eat', 'ate', 'tea'],
#  ['apt', 'pat'],
#  ['now']]


# Solution
# =====================================================================================================================
def anagram_sort(n):
    """
    anagram_sort: Sort a list of words by if they are an anagram of each other
    :param n: (List(strings)) - List containing words
    :return: (List(List(String))) - Nested list of strings grouped by if they are anagrams of each other
    """
    anagram_sorted = []

    # To add first word
    if not anagram_sorted:
        anagram_sorted.append([n[0]])

    # Checks every word in n
    for i in range(1, len(n)):
        # Boolean to check if anagram is already in the sorted list
        in_sorted = False
        # Checks every word already sorted
        for j in range(len(anagram_sorted)):
            if sorted(n[i]) == sorted(anagram_sorted[j][0]):
                anagram_sorted[j].append(n[i])
                in_sorted = True
        if not in_sorted:
            anagram_sorted.append([n[i]])

    return anagram_sorted


# Input
# =====================================================================================================================
print(anagram_sort(['eat', 'ate', 'apt', 'pat', 'tea', 'now']))
