# Problem
# =====================================================================================================================
# In chess, the Elo rating system is used to calculate player strengths based on game results.
# A simplified description of the Elo system is as follows.

# Every player begins at the same score. For each subsequent game,
# the loser transfers some points to the winner,
# where the amount of points transferred depends on how unlikely the win is.

# For example, a 1200-ranked player should gain much more points for beating a 2000-ranked player
# than for beating a 1300-ranked player.
# Implement this system.

# Solution
# =====================================================================================================================
def elo_calculator(elo1, elo2):
    """
    elo_calculator: Takes two chess elo's and returns what the updated elo's would like like if the game went either way
    :param elo1: (int) - elo of first player
    :param elo2: (int) - elo of second player
    :return: (list(pairs)) - List containing (Original, elo1 wins, elo2 wins) values
    """
    results = [(elo1, elo2)]
    elo_ratio = 0

    if elo1 < elo2:
        elo_ratio = elo1 / elo2
        gains = (elo2 * (1-elo_ratio)) - (elo1 * (1-elo_ratio))

        # elo 1 wins (worse player)
        results.append((elo1 + gains, elo2 - gains))

        # elo 2 wins (better player) gains 1/2
        results.append((elo1 - (.5 * gains), elo2 + (.5 * gains)))

        print(results)
        return results

    elif elo1 > elo2:
        elo_ratio = elo2 / elo1
        gains = (elo1 * (1-elo_ratio)) - (elo2 * (1-elo_ratio))

        # elo 1 wins (better player)
        results.append((elo1 + (.5 * gains), elo2 - (.5 * gains)))

        # elo 2 wins (worse player) gains 1/2
        results.append((elo1 - gains, elo2 + gains))

        print(results)
        return results

    # elo1 == elo2
    else:
        # elo 1 wins
        results.append((elo1 + (.01 * elo1), elo2 - (.01 * elo1)))
        # elo 2 wins
        results.append((elo1 - (.01 * elo1), elo2 + (.01 * elo1)))
        print(results)
        return results


# Input
# =====================================================================================================================
elo_calculator(1000, 1200)
elo_calculator(1000, 2000)

elo_calculator(1200, 1000)
elo_calculator(2000, 1000)

elo_calculator(1500, 1500)
