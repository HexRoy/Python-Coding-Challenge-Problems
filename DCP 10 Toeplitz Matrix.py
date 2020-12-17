# Problem
# =====================================================================================================================
# In linear algebra,
# a Toeplitz matrix is one in which the elements on any given diagonal from top left to bottom right are identical.
# Here is an example:
# 1 2 3 4 8
# 5 1 2 3 4
# 4 5 1 2 3
# 7 4 5 1 2
# Write a program to determine whether a given input is a Toeplitz matrix.


# Solution
# =====================================================================================================================

# First thoughts on solving:
#  1. Starting at [0,0] and working toward [0,n] (n being the last element in the row), check all diagonals to see if
#   all of the numbers are the same.
#  2. Next starting at [1,0] and working toward [n,0] (n being the last element in the column) check all diagonals to
#   see if all of the numbers are the same
#   This method should cover the entire matrix
#   Edge cases: top right corner/bottom left corner. Check one element/ skip entirely if we assume a valid input

def is_toeplitz_matrix(matrix):
    """
    is_toeplitz_matrix: Determines if a given matrix is a Toeplitz matrix
    :param matrix: a list of lists containing numbers
    :return: True if a Toeplitz matrix, If not False
    """
    rows = len(matrix)
    columns = len(matrix[0])
    checking = True

    # To check the first row diagonals in the matrix
    for i in range(columns):
        current_x = i
        current_y = 0
        current_value = matrix[0][i]
        while checking:
            if current_x < columns-1 and current_y < rows-1:
                if current_value == matrix[current_y+1][current_x+1]:
                    current_x += 1
                    current_y += 1
                else:
                    print("Not a Toeplitz matrix")
                    return False
            else:
                break
    # To check the first column of diagonals
    #   rows - 1 because we checked the first row in above loop
    for i in range(rows-1):
        current_x = 0
        current_y = i
        current_value = matrix[i][0]
        while checking:
            if current_x < columns-1 and current_y < rows-1:
                if current_value == matrix[current_y+1][current_x+1]:
                    current_x += 1
                    current_y += 1
                else:
                    print("Not a Toeplitz matrix")
                    return False
            else:
                break

    print("Is a Toeplitz matrix")
    return True


# Tests
# =====================================================================================================================

# Should pass
is_toeplitz_matrix([
                [1, 2, 3, 4, 8],
                [5, 1, 2, 3, 4],
                [4, 5, 1, 2, 3],
                [7, 4, 5, 1, 2]
                ])

# Should fail
is_toeplitz_matrix([
                [1, 2, 3, 4, 8],
                [5, 1, 2, 3, 4],
                [4, 1, 1, 2, 3],
                [7, 4, 5, 1, 2]
                ])
