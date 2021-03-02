# Problem
# =====================================================================================================================
# We have some historical clickstream data gathered from our site anonymously using cookies.
# The histories contain URLs that users have visited in chronological order.

# Write a function that takes two users' browsing histories as input
# and returns the longest contiguous sequence of URLs that appear in both.

# For example, given the following two users' histories:
# user1 = ['/home', '/register', '/login', '/user', '/one', '/two']
# user2 = ['/home', '/red', '/login', '/user', '/one', '/pink']
# You should return the following:
# ['/login', '/user', '/one']


# Solution
# =====================================================================================================================
def longest_sequence(ar1, ar2):
    """
    longest_sequence: Find the longest sequence both arrays have in commmon
    :param ar1: (list(string)) - A users history
    :param ar2: (list(string)) - A users history
    :return: (list(string)) - the longest common sequence in ar1 and ar2
    """
    len_ar1 = len(ar1)
    len_ar2 = len(ar2)
    max_sequence = 0
    sequence = None

    for i in range(len_ar1):
        for j in range(len_ar2):
            temp_max = 0
            temp_sequence = []
            temp_i = i
            temp_j = j

            # If the items in the list match
            if ar1[i] == ar2[j]:
                temp_max += 1
                temp_sequence.append(ar1[i])

                keep_checking = True
                while keep_checking:
                    # To keep inside bonds of array
                    if (temp_i + 1 > len_ar1) or (temp_j + 1 > len_ar2):
                        break

                    # Checks to see if the next index of both lists are the same
                    if ar1[temp_i+1] == ar2[temp_j+1]:
                        temp_i += 1
                        temp_j += 1
                        temp_max += 1
                        temp_sequence.append(ar1[temp_i])
                    else:
                        keep_checking = False

                if temp_max > max_sequence:
                    max_sequence = temp_max
                    sequence = temp_sequence

    return max_sequence, sequence


# Input
# =====================================================================================================================
print(longest_sequence(['/home', '/register', '/login', '/user', '/one', '/two'], ['/home', '/red', '/login', '/user', '/one', '/pink']))
