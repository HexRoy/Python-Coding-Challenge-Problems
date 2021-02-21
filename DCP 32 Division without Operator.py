# Problem
# =====================================================================================================================
# Implement integer division without using the division operator.
# Your function should return a tuple of (dividend, remainder) and it should take two numbers, the product and divisor.
# For example, calling divide(10, 3) should return (3, 1) since the divisor is 3 and the remainder is 1.


# Solution
# =====================================================================================================================
def divide(n, m):
    """
    divide: Divides n by m without using the division operator
    :param n: (int)
    :param m: (int)
    :return: (list) (Answer, Remainder)
    """
    result = [0, 0]
    temp = 0
    for i in range(n):
        if temp == m:
            temp = 0
            result[0] += 1
        temp += 1
    result[1] = temp

    return result


# Input
# =====================================================================================================================
print(divide(10, 3))
