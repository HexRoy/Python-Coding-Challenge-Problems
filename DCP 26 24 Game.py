# Problem
# =====================================================================================================================
# The 24 game is played as follows. You are given a list of four integers, each between 1 and 9, in a fixed order.
# By placing the operators +, -, *, and / between the numbers, and grouping them with parentheses,
# determine whether it is possible to reach the value 24.

# For example, given the input [5, 2, 7, 8], you should return True, since (5 * 2 - 7) * 8 = 24.
# Write a function that plays the 24 game.


# Solution
# =====================================================================================================================
from itertools import product


def twenty_four_game(n):
    """
    twenty_four_game: Checks if the input can equate to 24 with any given set of operators
    :param n: (list(ints)) List of 4 ints
    :return: None, Prints out the solutions
    """
    operators = ['+', '-', '*', '/']

    # Creates all possible arrangements of the operators
    ops = product(operators, repeat=(len(n)-1))
    for op_set in ops:
        # Creates the initial expression
        expression = str(n[0]) + op_set[0] + str(n[1]) + op_set[1] + str(n[2]) + op_set[2] + str(n[3])

        # Checks original expression
        if eval(expression) == 24:
            print(expression, '= 24')

        # Checks every combination with parentheses
        for i in range(len(expression)):
            for j in range(i+1, len(expression)+1):
                if i == 0 and j % 2 != 0:
                    if eval('(' + expression[i:j] + ')' + expression[j:]) == 24:
                        print('(' + expression[i:j] + ')' + expression[j:], '= 24')

                elif i % 2 == 0 and j % 2 != 0:
                    if eval(expression[:i] + '(' + expression[i:j] + ')' + expression[j:]) == 24:
                        print(expression[:i] + '(' + expression[i:j] + ')' + expression[j:], '= 24')


# Input
# =====================================================================================================================
twenty_four_game([5, 2, 7, 8])

