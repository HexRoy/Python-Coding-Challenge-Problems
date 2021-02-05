# Problem
# =====================================================================================================================
# Given integers M and N, write a program that counts how many
# positive integer pairs (a, b) satisfy the following conditions:
# •	a + b = M
# •	a XOR b = N


# Solution
# =====================================================================================================================
def add_xor_pairs(m, n):
    """
    add_xor_pairs: Finds how many pairs that will add to m and xor to n
    :param m: The result of A + B (A, B being the pair produced for the solution)
    :param n: The result of A XOR B (A, B being the pair produced for the solution)
    :return: Number of pairs to satisfy m, n
    """
    total = 0
    for a in range(int(m/2) + 1):
        for b in range(m):
            if a + b == m:
                if a ^ b == n:
                    print('Pair Found: ', a, b)
                    total += 1

    return total


# Input
# =====================================================================================================================
print(add_xor_pairs(17, 13))

