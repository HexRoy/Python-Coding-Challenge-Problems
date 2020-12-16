# Problem
# =====================================================================================================================
# You are given an array representing the heights of neighboring buildings on a city street, from east to west.
# The city assessor would like you to write an algorithm
# that returns how many of these buildings have a view of the setting sun, in order to properly value the street.

# For example, given the array [3, 7, 8, 3, 6, 1], you should return 3,
# since the top floors of the buildings with heights 8, 6, and 1 all have an unobstructed view to the west.

# Can you do this using just one forward pass through the array?


# Solution
# =====================================================================================================================
def sunset_view(building_heights):
    """
    sunset_view: find how many building have a sunset view in the array
    :param building_heights: list of heights of building
    :return: the number of buildings in building_heights that have a sunset view
    """
    total_sunset_view = 0
    last_highest = None
    for i in range(len(building_heights)):
        if building_heights[i] == max(building_heights[i:]):
            if last_highest is None:
                last_highest = building_heights[i]
                total_sunset_view += 1
            elif building_heights[i] < last_highest:
                last_highest = building_heights[i]
                total_sunset_view += 1
    print(total_sunset_view)


# Tests
# =====================================================================================================================
sunset_view([3, 7, 8, 3, 6, 1])
sunset_view([3, 7, 8, 3, 6, 1, 1])
