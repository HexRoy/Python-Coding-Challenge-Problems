# Problem
# =====================================================================================================================
# The "look and say" sequence is defined as follows: beginning with the term 1,
# each subsequent term visually describes the digits appearing in the previous term. The first few terms are as follows:
# 1
# 11
# 21
# 1211
# 111221

# As an example, the fourth term is 1211, since the third term consists of one 2 and one 1.
# Given an integer N, print the Nth term of this sequence.


# Solution
# =====================================================================================================================
def look_and_say(n):
    """
    look_and_say: Finds the nth term in the look and say sequence
    :param n: (Int) What term to find
    :return: (String) The nth term in the sequence
    """

    # Base Case
    if n == 1:
        return 1

    current_number = '1'
    next_number = ''

    # Loops through number in the sequence
    for i in range(n-1):
        current_chunk = ''

        # Loops though the digits in the previous number
        for j in range(len(current_number)):
            current_digit = current_number[j]

            # If we are not at the end of the number
            if j + 1 != len(current_number):

                # if the next digit is the same as our current
                if current_digit == current_number[j+1]:
                    current_chunk += current_number[j+1]
                else:
                    current_chunk += current_digit
                    total = str(len(current_chunk))
                    next_number += total + current_digit
                    current_chunk = ''
            else:
                current_chunk += current_digit
                total = str(len(current_chunk))
                next_number += total + current_digit

        current_number = next_number
        next_number = ''

    return current_number


# Input
# =====================================================================================================================
for x in range(10):
    print(look_and_say(x+1))
