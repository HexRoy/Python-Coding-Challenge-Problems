# Problem
# =====================================================================================================================
# Given a string, find the length of the smallest window that contains every distinct character.
# Characters may appear more than once in the window.
# For example, given "jiujitsu", you should return 5, corresponding to the final five letters.


# Solution
# =====================================================================================================================
def size_smallest_substring(word):
    """
    size_smallest_substring: Find the size of the smallest substring containing every unique letter in the word
    :param word: (String) The word to find the smallest substring of
    :return: (Int) Size of the smallest substring
    """
    length = None
    all_unique_letters = []

    # Gets all of the letters into a dictionary
    for letter in word:
        if letter not in all_unique_letters:
            all_unique_letters.append(letter)
    all_unique_letters.sort()

    # Loop through each combination to find a list matching the unique letters
    #   If matching, keep the shortest length
    for i in range(len(word)):
        for j in range(i, len(word)):
            current_letters = []
            for letter in word[i:j+1]:
                if letter not in current_letters:
                    current_letters.append(letter)
            current_letters.sort()
            if current_letters == all_unique_letters:
                if length is None:
                    length = (j-i) + 1
                elif ((j-i) + 1) < length:
                    length = (j-i) + 1

    print("Shortest: ", length)
    return length

# Input
# =====================================================================================================================
size_smallest_substring('jiujitsu')
size_smallest_substring('eeeee')
