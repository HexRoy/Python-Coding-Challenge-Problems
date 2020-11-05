# Given an integer k and a string s,
# find the length of the longest substring that contains at most k distinct characters.
# For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".

import itertools

def longest_substring(k, my_string):
    current_longest = 0
    current_longest_pair = []
    current_longest_string = ""
    letters = list(set(my_string))

    # Loop through every combination of letters in the string
    for letters in itertools.combinations(letters, k):
        for i in range(len(my_string)):
            current = 0
            if my_string[i] in letters:
                current += 1

                while i+current < len(my_string):
                    if my_string[i + current] in letters:
                        current += 1

                    else:
                        break

            if current > current_longest:
                current_longest_pair = letters
                current_longest = current
                current_longest_string = my_string[i:i+current]

    print(current_longest)
    print(current_longest_pair)
    print(current_longest_string)

longest_substring(2,"abcbcbca")
longest_substring(3, "abcabcdf")