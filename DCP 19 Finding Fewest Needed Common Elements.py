# Problem
# =====================================================================================================================
# At a popular bar, each customer has a set of favorite drinks, and will happily accept any drink among this set.
# For example, in the following situation, customer 0 will be satisfied with drinks 0, 1, 3, or 6.
# preferences = {
#     0: [0, 1, 3, 6],
#     1: [1, 4, 7],
#     2: [2, 4, 7, 5],
#     3: [3, 2, 5],
#     4: [5, 8]
# }
# A lazy bartender working at this bar is trying to reduce his effort by limiting the drink recipes he must memorize.
# Given a dictionary input such as the one above,
# return the fewest number of drinks he must learn in order to satisfy all customers.
# For the input above, the answer would be 2, as drinks 1 and 5 will satisfy everyone.


# Solution
# =====================================================================================================================
from itertools import combinations


def fewest_common_drinks(n):
    drink_list = list(set([y for x in list(n.values()) for y in x]))

    # Loop to get the different sizes of possible drink combos
    for i in range(len(n)):
        comb = combinations(drink_list, i+1)

        # Loops through each combo
        for drink_combo in comb:
            common_counter = 0
            person_satisfied = []

            # Loops through the drink in the drink combo
            for drink in drink_combo:

                # Loops to check each person in the dictionary
                for j in range(len(n)):
                    if drink in list(n.values())[j]:
                        if j not in person_satisfied:
                            common_counter += 1
                            person_satisfied.append(j)
                        if common_counter == len(n):
                            print("Best Combo Found: ", drink_combo)
                            return drink_combo


# Input
# =====================================================================================================================
fewest_common_drinks({
     0: [0, 1, 3, 6],
     1: [1, 4, 7],
     2: [2, 4, 7, 5],
     3: [3, 2, 5],
     4: [5, 8]
 })
