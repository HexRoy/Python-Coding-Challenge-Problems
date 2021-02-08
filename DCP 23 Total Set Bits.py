# Problem
# =====================================================================================================================
# Write an algorithm that finds the total number of set bits in all integers between 1 and N.


# Solution
# =====================================================================================================================
def total_set_bits(n):
    """
    total_set_bits: Finds the total number of set bits between 1 - n (1 and n inclusive)
    :param n: (Int) the upper limit we will find the set bits for
    :return: (Int)  Total number of set bits
    """
    set_bits = 0

    if n < 1:
        exit(1)

    if n == 1:
        return 1

    for i in range(1, n+1):
        binary = bin(i).replace('0b', '')
        for j in range(len(binary)):
            if binary[j] == '1':
                set_bits += 1
    return set_bits


# Input
# =====================================================================================================================
print(total_set_bits(10))
