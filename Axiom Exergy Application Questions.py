# Geoffroy Penny
#   JR Software Engineer: Axiom Exergy

# ======================================================================================================================
# Problem 1
# ======================================================================================================================


def roman_to_arabic(roman_numeral):
    """
    roman_to_arabic: computes the Arabic numerical equivalent for the given roman numeral input
    :param roman_numeral: ASSUMES THERE IS A VALID INPUT: Capitalized valid roman numeral
    :return: Arabic numerical equivalent of the roman numeral input
    """

    arabic = 0
    conversion = {'I': 1,
                  'V': 5,
                  'X': 10,
                  'L': 50,
                  'C': 100,
                  'D': 500,
                  'M': 1000,
                  }

    for i in range(len(roman_numeral)):
        if i == 0:
            arabic += conversion[roman_numeral[i]]
        # If the current is less than or equal to the previous, simply add the amount
        elif conversion[roman_numeral[i]] <= conversion[roman_numeral[i-1]]:
            arabic += conversion[roman_numeral[i]]
        # If the current is more than the previous, you need to subtract double the amount from the current
        else:
            arabic += conversion[roman_numeral[i]] - (2 * conversion[roman_numeral[i-1]])

    print(arabic)
    return arabic


# ======================================================================================================================
# Problem 2
# ======================================================================================================================

def calc_profit(param_list):
    """
    calc_profit: the formula for profits
    :param param_list: contains the price per acre of: corn, oats. followed by the number of acres of: corn, oats
    :return: the profits
    """
    price_corn = param_list[0]
    price_oats = param_list[1]
    acre_corn = param_list[2]
    acre_oats = param_list[3]
    total = (price_corn * acre_corn) + (price_oats * acre_oats)
    return int(total)


def solve_equation(x, y, p1, p2, h1, h2):
    """
    solve_equation: compute various scenarios for the following optimization problem
    :param x: acres of land
    :param y: hours of labor available
    :param p1: dollars per acre of corn
    :param p2: dollars per acre of oats
    :param h1: hours of labor per acre of corn
    :param h2: hours of labor per acre of oats
    :return: how many acres of each crop can be plated to maximize profits
    """
    # This is a brute force method
    acres_corn = 0
    acres_oats = 0
    best_profit = 0
    for i in range(1, x):
        for j in range(x):
            parameters = [p1, p2, i, j]
            if i + j <= x:                                          # Acres of corn + oats < total acres
                if(i*h1 + j*h2) <= y:                               # Hours of corn + oats < total hours
                    if calc_profit(parameters) > best_profit:       # Current profit > best profit
                        acres_corn = i
                        acres_oats = j
                        best_profit = calc_profit(parameters)
    print('Profits: %d, using %d acres of corn and %d acres of oats' % (best_profit, acres_corn, acres_oats))


# ======================================================================================================================
# Function Calls
# ======================================================================================================================

roman_to_arabic("MDCCLXXVI")
solve_equation(240, 320, 40, 30, 2, 1)
solve_equation(300, 380, 70, 45, 3, 1)
solve_equation(180, 420, 65, 55, 3, 2)
