# Problem
# =====================================================================================================================
# Using a function rand5() that returns an integer from 1 to 5 (inclusive) with uniform probability,
# implement a function rand7() that returns an integer from 1 to 7 (inclusive).


# Solution
# =====================================================================================================================
from random import randint


def rand5():
    """
    rand5: Return a random int from 1-5 inclusive
    :return: (Int) From 1-5
    """
    return randint(1, 5)


def rand7():
    """
    rand7(): Using rand5 return a random int from 1-7 inclusive
    :return: (Int) From 1 - 7
    """
    rand_5 = rand5()
    additional = randint(0, 2)
    return rand_5 + additional

# Input
# =====================================================================================================================
for i in range(20):
    print(rand7())
