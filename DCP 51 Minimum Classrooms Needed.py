# Problem
# =====================================================================================================================
# Given an array of time intervals (start, end) for classroom lectures (possibly overlapping),
# find the minimum number of rooms required.
# For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.


# Solution
# ====================================================================================================================
from operator import itemgetter


def min_number_classrooms(time_list):
    """
    min_number_classrooms: Finds minimum number of classrooms needed for each class to not share a room
    :param time_list: (List(Tuples)) - Tuples are representing start - end times of each class
    :return: (Int) - The minimum number of classrooms needed
    """
    min_classrooms = 0

    if len(time_list) == 1:
        return 1

    # Sort list by start times
    time_list.sort(key=itemgetter(0))
    print(time_list)
    for i in range(len(time_list)):
        temp_min = 0
        i_start = time_list[i][0]
        i_end = time_list[i][1]

        for j in range(i, len(time_list)):
            j_start = time_list[j][0]
            j_end = time_list[j][1]

            if (i_start <= j_start <= i_end) or (i_start <= j_end <= i_end):
                temp_min += 1

        if temp_min > min_classrooms:
            min_classrooms = temp_min

    return min_classrooms


# Input
# =====================================================================================================================
print(min_number_classrooms([(30, 75), (0, 50), (60, 150)]))
print(min_number_classrooms([(30, 75), (0, 50), (60, 150), (60, 160), (161, 1000)]))
