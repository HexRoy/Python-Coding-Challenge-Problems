# Given an array of integers, determine whether it contains a Pythagorean triplet.
# Recall that a Pythogorean triplet (a, b, c) is defined by the equation a2+ b2= c2.


# Solution
# ================================================================================================================
def triple_check(a, b, c):
    if type(a) == int and type(b) == int and type(c) == int:
        int_list = [a, b, c]
        int_list.sort()
        if int_list[0]**2 + int_list[1]**2 == int_list[2]**2:
            print(a, b, c, "Pass, pythogorean triplet found", int_list)
        else:
            print("Fail, Not pythogorean triplet found", int_list)
    else:
        print('Invalid Input: must be integers')
        return


# Tests, with random orders
triple_check(3, 4, 5)       # Pass
triple_check(5, 4, 3)       # Pass
triple_check(4, 3, 5)       # Pass
triple_check(4, 6, 5)       # Fail
triple_check(4, 'a', 5)     # Fail

triple_check(5, 13, 12)     # Pass
triple_check(12, 5, 13)     # Pass
triple_check(13, 12, 5)     # Pass
triple_check(13, 123, 5)    # Fail
triple_check(13, "4d", 5)   # Fail
