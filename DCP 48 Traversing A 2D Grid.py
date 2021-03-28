# Problem
# =====================================================================================================================
# You are in an infinite 2D grid where you can move in any of the 8 directions:
#  (x,y) to
#     (x+1, y),
#     (x - 1, y),
#     (x, y+1),
#     (x, y-1),
#     (x-1, y-1),
#     (x+1,y+1),
#     (x-1,y+1),
#     (x+1,y-1)
# You are given a sequence of points and the order in which you need to cover the points.
# Give the minimum number of steps in which you can achieve it. You start from the first point.
# Example:
# Input: [(0, 0), (1, 1), (1, 2)]
# Output: 2
# It takes 1 step to move from (0, 0) to (1, 1). It takes one more step to move from (1, 1) to (1, 2).


# Solution
# =====================================================================================================================
def number_of_steps(n):
    """
    number_of_steps: Find the number of steps between n[0] -> n[1]... -> n[x] (x being the ending point in the array)
    :param n: (List(Tuples)) List containing points on a 2D grid
    :return: (Int) Number of steps required to reach each point in the list
    """
    if len(n) == 1:
        return 0

    total_steps = 0

    # Loops through each point in the list
    for i in range(1, len(n)):
        goal = list(n[i])
        current = list(n[i-1])
        temp_steps = 0

        # Calculates how many steps it takes between points
        while goal != current:
            temp_steps += 1

            if goal[0] == current[0]:
                if goal[1] > current[1]:
                    current[1] += 1
                else:
                    current[1] -= 1

            elif goal[1] == current[1]:
                if goal[0] > current[0]:
                    current[0] += 1
                else:
                    current[0] -= 1

            elif (goal[0] > current[0]) and (goal[1] > current[1]):
                current[0] += 1
                current[1] += 1

            elif (goal[0] > current[0]) and (goal[1] < current[1]):
                current[0] += 1
                current[1] -= 1

            elif (goal[0] < current[0]) and (goal[1] > current[1]):
                current[0] -= 1
                current[1] += 1

            elif (goal[0] < current[0]) and (goal[1] < current[1]):
                current[0] -= 1
                current[1] -= 1

        total_steps += temp_steps

    return total_steps


# Input
# =====================================================================================================================
print(number_of_steps([(0, 0), (1, 1), (1, 2)]))
