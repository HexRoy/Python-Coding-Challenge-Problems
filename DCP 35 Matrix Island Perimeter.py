# Problem
# =====================================================================================================================
# You are given a 2D matrix of 1s and 0s where 1 represents land and 0 represents water.
# Grid cells are connected horizontally or vertically (not diagonally).
# The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

# An island is a group is cells connected horizontally or vertically, but not diagonally.
# There is guaranteed to be exactly one island in this grid, and the island doesn't have
# water inside that isn't connected to the water around the island. Each cell has a side length of 1.

# Determine the perimeter of this island.
# For example, given the following matrix:
# [[0, 1, 1, 0],
# [1, 1, 1, 0],
# [0, 1, 1, 0],
# [0, 0, 1, 0]]
# Return 14.


# Solution
# =====================================================================================================================
def island_perimeter(matrix):
    perimeter = 0
    height = len(matrix)
    width = len(matrix[0])

    for i in range(height):
        for j in range(width):
            if matrix[i][j] == 1:

                # If its on the top row
                if i == 0:
                    perimeter += 1

                    if j == 0:
                        perimeter += 1
                        if matrix[i][j + 1] != 1:
                            perimeter += 1
                        if matrix[i + 1][j] != 1:
                            perimeter += 1

                    elif j == width:
                        perimeter += 1
                        if matrix[i][j - 1] != 1:
                            perimeter += 1
                        if matrix[i + 1][j] != 1:
                            perimeter += 1

                    else:
                        if matrix[i][j - 1] != 1:
                            perimeter += 1
                        if matrix[i][j + 1] != 1:
                            perimeter += 1
                        if matrix[i + 1][j] != 1:
                            perimeter += 1

                # If its on the bottom
                elif i == height - 1:
                    perimeter += 1

                    if j == 0:
                        perimeter += 1
                        if matrix[i - 1][j] != 1:
                            perimeter += 1
                        if matrix[i][j + 1] != 1:
                            perimeter += 1

                    elif j == width:
                        perimeter += 1
                        if matrix[i][j - 1] != 1:
                            perimeter += 1
                        if matrix[i - 1][j] != 1:
                            perimeter += 1
                    else:
                        if matrix[i][j - 1] != 1:
                            perimeter += 1
                        if matrix[i][j + 1] != 1:
                            perimeter += 1
                        if matrix[i - 1][j] != 1:
                            perimeter += 1

                # If its on the left
                elif j == 0:
                    perimeter += 1

                    if i == 0:
                        perimeter += 1
                        if matrix[i][j + 1] != 1:
                            perimeter += 1
                        if matrix[i + 1][j] != 1:
                            perimeter += 1

                    if i == height:
                        perimeter += 1
                        if matrix[i - 1][j] != 1:
                            perimeter += 1
                        if matrix[i][j + 1] != 1:
                            perimeter += 1

                    else:
                        if matrix[i - 1][j] != 1:
                            perimeter += 1
                        if matrix[i + 1][j] != 1:
                            perimeter += 1
                        if matrix[i][j + 1] != 1:
                            perimeter += 1

                elif j == width - 1:
                    perimeter += 1

                    if i == 0:
                        perimeter += 1
                        if matrix[i][j - 1] != 1:
                            perimeter += 1
                        if matrix[i + 1][j] != 1:
                            perimeter += 1

                    if i == height:
                        perimeter += 1
                        if matrix[i - 1][j] != 1:
                            perimeter += 1
                        if matrix[i][j - 1] != 1:
                            perimeter += 1

                    else:
                        if matrix[i - 1][j] != 1:
                            perimeter += 1
                        if matrix[i + 1][j] != 1:
                            perimeter += 1
                        if matrix[i][j - 1] != 1:
                            perimeter += 1

                else:
                    if matrix[i - 1][j] != 1:
                        perimeter += 1
                    if matrix[i + 1][j] != 1:
                        perimeter += 1
                    if matrix[i][j - 1] != 1:
                        perimeter += 1
                    if matrix[i][j + 1] != 1:
                        perimeter += 1
    return perimeter


# Input
# =====================================================================================================================
print(island_perimeter([[0, 1, 1, 0],
                        [1, 1, 1, 0],
                        [0, 1, 1, 0],
                        [0, 0, 1, 0]]
                       ))
