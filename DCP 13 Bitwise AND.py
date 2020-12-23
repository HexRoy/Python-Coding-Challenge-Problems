# Problem
# =====================================================================================================================
# Write a function that returns the bitwise AND of all integers between M and N, inclusive.


# Solution
# =====================================================================================================================
def calculate_bitwise_and(a, b):
    """
    bitwise_and: Calculates the BITWISE AND of two given numbers
    :param a: (int) Any integer to be used for bitwise AND calculation
    :param b: (int) Any integer to be used for bitwise AND calculation
    :return: (int) The bitwise AND of (a,b)
    """
    a = convert_to_binary(a)
    b = convert_to_binary(b)

    a, b = same_size(a, b)

    bitwise_and = None
    for i in range(len(a)):
        if bitwise_and is not None:
            if a[i] == '1' and b[i] == '1':
                bitwise_and += '1'
            else:
                bitwise_and += '0'
        else:
            if a[i] == 1 and b[i] == 1:
                bitwise_and = '1'
            else:
                bitwise_and = '0'

    print('Bitwise AND (Binary): ', bitwise_and + '\nBitwise AND (Integer): ', convert_to_numeric(bitwise_and))
    return convert_to_numeric(bitwise_and)


def same_size(a, b):
    """
    same_size: Converts the binary numbers to the same length by prepending zeros to the smaller one
    :param a: (string) Binary number
    :param b: (string) Binary number
    :return: (strings) Binary numbers a,b however they are the same length
    """
    if len(a) == len(b):
        return a, b
    elif len(a) < len(b):
        new_a = a
        for i in range(len(b) - len(a)):
            new_a = '0' + new_a
        return new_a, b
    else:
        new_b = b
        for i in range(len(a) - len(b)):
            new_b = '0' + new_b
        return a, new_b


def convert_to_binary(n):
    """
    convert_to_binary: Returns the binary value of the number inputted
    :param n: (int) Number as integer to be converted to binary
    :return: (string) The binary representation of the given number. As a string
    """
    return bin(n)[2:]


def convert_to_numeric(n):
    """
    convert_to_numeric: Returns the integer value of the 2 based binary number inputted
    :param n: (string) Number as binary to be converted to an int
    :return: (int) The integer representation of the given number
    """
    return int(n, 2)


# Input
# =====================================================================================================================
calculate_bitwise_and(12, 25)
calculate_bitwise_and(142342, 2432525)
