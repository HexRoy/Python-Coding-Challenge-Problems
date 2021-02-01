# Problem
# =====================================================================================================================
# A strobogrammatic number is a positive number that appears the same after being rotated 180 degrees.
# For example, 16891 is strobogrammatic.
# Create a program that finds all strobogrammatic numbers with N digits.


# Solution
# =====================================================================================================================
# All strobogrammatic numbers: 0, 1, 6, 8, 9
#   0 = 0
#   1 = 1
#   6 = 9
#   8 = 8

def find_strobogrammatic(n):
    """
    find_strobogrammatic: Finds all strobogrammatic numbers with n digits
    :param n: (Int) The number of digits to search up to
    :return: (List[Int]) Containing strobogrammatic numbers with <= n digits
    """
    strobogrammatic_nums = ['0', '1', '6', '8', '9']
    strobogrammatic_convert_69 = {'6': '9',
                                  '9': '6'}
    strobogrammatic_nums_in_n = []
    for i in range(1, ((10**n)-1)):
        number_length = len(str(i))
        for j in range(number_length):
            if str(i)[j] in strobogrammatic_nums:
                if j == number_length-1:
                    reverse = str(i)[::-1]

                    # For single length numbers
                    if number_length == 1:
                        if i == 1 or i == 8:
                            strobogrammatic_nums_in_n.append(i)
                    # For even length numbers
                    elif number_length % 2 == 0:
                        for k in range(int(number_length/2)):
                            compare_to_index = (int(number_length) - 1 - k)
                            if str(i)[k] == '0' or str(i)[k] == '1' or str(i)[k] == '8':
                                if str(i)[k] == str(i)[compare_to_index]:
                                    if k == int(number_length/2) - 1:
                                        strobogrammatic_nums_in_n.append(i)
                                else:
                                    break
                            else:
                                if strobogrammatic_convert_69[str(i)[k]] == str(i)[compare_to_index]:
                                    if k == int(number_length / 2) - 1:
                                        strobogrammatic_nums_in_n.append(i)
                                else:
                                    break

                    # For odd length numbers
                    else:
                        for k in range(int(number_length / 2)):
                            compare_to_index = (int(number_length) - 1 - k)
                            if str(i)[k] == '0' or str(i)[k] == '1' or str(i)[k] == '8':
                                if str(i)[k] == str(i)[compare_to_index]:
                                    if k == int(number_length / 2) - 1:
                                        if str(i)[int(number_length / 2)] == '0' or str(i)[int(number_length / 2)] == '1' or str(i)[int(number_length / 2)] == '8':
                                            strobogrammatic_nums_in_n.append(i)
                                else:
                                    break
                            else:
                                if strobogrammatic_convert_69[str(i)[k]] == str(i)[compare_to_index]:
                                    if k == int(number_length / 2) - 1:
                                        if str(i)[int(number_length / 2)] == '0' or str(i)[int(number_length / 2)] == '1' or str(i)[int(number_length / 2)] == '8':
                                            strobogrammatic_nums_in_n.append(i)
                                else:
                                    break

            # Not a strobogrammatic number
            else:
                break
    print(strobogrammatic_nums_in_n)
    return strobogrammatic_nums_in_n


# Input
# =====================================================================================================================

find_strobogrammatic(5)