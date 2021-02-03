# Problem
# =====================================================================================================================
# Given an integer n, find the next biggest integer with the same number of 1-bits on.
# For example, given the number 6 (0110 in binary), return 9 (1001).


# Solution
# =====================================================================================================================
def next_largest(n):
    """
    next_largest: Finds the next largest binary number with the same amount of 1's
    :param n: (int) number to find the next largest from
    :return: (int) the next largest number
    """
    binary = bin(n).replace("0b", "")
    target_1s = binary.count('1')

    if target_1s == 0:
        return 0

    temp = n + 1
    while True:
        temp_binary = bin(temp).replace('0b', '')
        temp_1s = temp_binary.count('1')
        if target_1s == temp_1s:
            return temp
        temp += 1


# Input
# =====================================================================================================================
print(next_largest(6))
print(next_largest(3))
print(next_largest(0))

