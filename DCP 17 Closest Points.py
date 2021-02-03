# Problem
# =====================================================================================================================
# Given a set of points (x, y) on a 2D cartesian plane, find the two closest points.
# For example, given the points [(1, 1), (-1, -1), (3, 4), (6, 1), (-1, -6), (-4, -3)], return [(-1, -1), (1, 1)].

# Solution
# =====================================================================================================================
from itertools import combinations


def closest_points(points):
    """
    closest_points: Finds the two closest points of a given set of points
    :param points: array containing points with (x,y) coordinates
    :return: List containing the two closest points
    """
    combs = combinations(points, 2)
    smallest_distance = None
    two_closest_points = None
    for x in combs:
        temp = distance_between(x)
        if smallest_distance is None or temp < smallest_distance:
            two_closest_points = x
            smallest_distance = temp
    print("The two closest points are: ", two_closest_points, '\nThey are: ', smallest_distance, ' apart')
    return two_closest_points


def distance_between(points):
    """
    distace_between: Finds the distance between two points
    :param points: List of 2 points
    :return: The distance between the two given points
    """
    return abs(points[0][0] - points[1][0]) + abs(points[0][1] - points[1][1])


# Input
# =====================================================================================================================
closest_points([(3, 4), (6, 1), (-1, -6), (-4, -3), (1, 1), (-1, -1)])
