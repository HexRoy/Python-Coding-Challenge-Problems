# Problem
# =====================================================================================================================
# You are given a list of (website, user) pairs that represent users visiting websites.
# Come up with a program that identifies the top k pairs of websites with the greatest similarity.
# For example, suppose k = 1, and the list of tuples is:
# [('a', 1), ('a', 3), ('a', 5),
#  ('b', 2), ('b', 6),
#  ('c', 1), ('c', 2), ('c', 3), ('c', 4), ('c', 5)
#  ('d', 4), ('d', 5), ('d', 6), ('d', 7),
#  ('e', 1), ('e', 3), ('e': 5), ('e', 6)]
# Then a reasonable similarity metric would most likely conclude that a and e are the most similar,
# so your program should return a e.


# Solution
# =====================================================================================================================
import operator
def most_similar(k, website_users):
    """
    most_similar: Finds k pairs of most similar websites based on users
    :param k: (int) Number of website pairs
    :param website_users: (list(tuples)) List of (website, user) pairs
    :return: (list(tuples)) k most similar website pairs
    """

    pairs = {}
    similar_pairs = []
    # Obtains the pairs and creates dictionary with amount of similarities
    for i in range(len(website_users)):
        for j in range(i, len(website_users)):
            if website_users[i][0] != website_users[j][0]:
                key = website_users[i][0] + website_users[j][0]

                # Each similar user is weighted 1
                if website_users[i][1] == website_users[j][1]:
                    if key in pairs:
                        pairs[key] += 1
                    else:
                        pairs[key] = 1

                # Each non similar user is weighted -.001
                else:
                    if key in pairs:
                        pairs[key] -= .001
                    else:
                        pairs[key] = -.001

    for i in range(k):
        similar_pairs.append(max(pairs, key=pairs.get))
        pairs.pop(max(pairs, key=pairs.get))

    print(similar_pairs)
    return similar_pairs


# Input
# =====================================================================================================================
most_similar(1,
             [('a', 1), ('a', 3), ('a', 5),
              ('b', 2), ('b', 6),
              ('c', 1), ('c', 2), ('c', 3), ('c', 4), ('c', 5),
              ('d', 4), ('d', 5), ('d', 6), ('d', 7),
              ('e', 1), ('e', 3), ('e', 5), ('e', 6)])

most_similar(4,
             [('a', 1), ('a', 3), ('a', 5),
              ('b', 2), ('b', 6),
              ('c', 1), ('c', 2), ('c', 3), ('c', 4), ('c', 5),
              ('d', 4), ('d', 5), ('d', 6), ('d', 7),
              ('e', 1), ('e', 3), ('e', 5), ('e', 6)])
