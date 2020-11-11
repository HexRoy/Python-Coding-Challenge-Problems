# Problem:
# Given a 32-bit positive integer N, determine whether it is a power of four in faster than O(log N) time.

# Solution:
def fourth_root(n):
    return True if (n**.25) % 1 == 0 else False


# Test Cases. We assume a valid input (integer)
test1 = 16   # 2 ^ 4
test2 = 81   # 3 ^ 4
test3 = 256  # 4 ^ 4
test4 = 257  # 4 ^ 4
test5 = 4  # 4 ^ 4
if fourth_root(test1):
    print('T')
if fourth_root(test2):
    print('T')
if fourth_root(test3):
    print('T')
if fourth_root(test4):
    print('T')
if fourth_root(test5):
    print('T')

