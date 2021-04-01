# Problem
# =====================================================================================================================
# A number is considered perfect if its digits sum up to exactly 10.
# Given a positive integer n, return the n-th perfect number.
# For example, given 1, you should return 19. Given 2, you should return 28.


# Solution
# ====================================================================================================================
def nth_perfect_number(n):
    i = 18
    nth_number = 0
    current_perfect_num = None
    while nth_number < n:
        if is_sum_ten(i):
            current_perfect_num = i
            nth_number += 1
        i += 1
    return current_perfect_num


def is_sum_ten(n):
    total = 0
    for digit in str(n):
        total += int(digit)
    if total == 10:
        return True
    return False


# Input
# =====================================================================================================================
print(nth_perfect_number(1))
print(nth_perfect_number(2))
