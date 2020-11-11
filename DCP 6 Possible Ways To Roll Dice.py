# Write a function, throw_dice(N, faces, total)
# That determines how many ways it is possible to throw N dice with some number of faces each to get a specific total.
# For example, throw_dice(3, 6, 7) should equal 15.

# Solution
# ====================================================================================================================
from itertools import product


def throw_dice(n, faces, total):
    """
    throw_dice:
    :param n: the number of dice
    :param faces: the number range (1 - faces)
    :param total: the target number
    :return: the total number of ways to reach the target number with given input
    """
    die_faces = []
    number_of_ways = 0
    ways = []

    # Input validation
    if total < n:
        print("Total cannot be less than minimum outcome")
        exit(1)
    if total > (n * faces):
        print("Total cannot be more than max outcome")
        exit(1)

    # Create a list for the die faces
    for i in range(1, faces+1):
        die_faces.append(i)

    # Find product of all combinations of die faces
    for i in product(die_faces, repeat=n):
        if sum(i) == total:
            number_of_ways += 1
            ways.append(i)

    print(number_of_ways)
    print(ways)

throw_dice(3, 6, 7)
