# Problem
# =====================================================================================================================
# Given a positive integer N, find the smallest number of steps it will take to reach 1.
# There are two kinds of permitted steps:
# •	You may decrement N to N - 1.
# •	If a * b = N, you may decrement N to the larger of a and b.
# For example, given 100, you can reach 1 in five steps with the following route: 100 -> 10 -> 9 -> 3 -> 2 -> 1.


# Solution
# ====================================================================================================================

# Find factors of n
#   If odd amount, use middle number (perfect square)
#   If even amount use the higher of the middle two

# If only 2 factors subtract 1 instead
def min_steps_to_one(n):
    current = n
    step = 0
    while current != 1:
        factors = find_factors(current)

        if len(factors) == 2:
            current -= 1
            step += 1
        else:
            current = factors[int((len(factors)/2))]
            step += 1
    return step


def find_factors(n):
    factors = []
    for i in range(1, n+1):
        if n % i == 0:
            factors.append(i)
    return factors


# Input
# =====================================================================================================================
print(min_steps_to_one(100))
print(min_steps_to_one(1000))
