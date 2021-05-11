
def linear_search(num_list, target):
    for index, num in enumerate(num_list):
        if num == target:
            return index


def binary_search(num_list, target):
    left_index = 0
    right_index = len(num_list) - 1
    middle_index = 0

    while left_index <= right_index:
        middle_index = (left_index + right_index) // 2
        mid_number = num_list[middle_index]

        if mid_number == target:
            return middle_index

        if mid_number < target:
            left_index = middle_index + 1
        else:
            right_index = middle_index - 1


def binary_search_recursive(num_list, target, left_index, right_index):
    if right_index < left_index:
        return -1

    middle_index = (left_index + right_index) // 2
    if middle_index >= len(num_list) or middle_index < 0:
        return -1

    mid_number = num_list[middle_index]

    if mid_number == target:
        return middle_index

    if mid_number < target:
        left_index = middle_index + 1
    else:
        right_index = middle_index - 1

    return binary_search_recursive(num_list, target, left_index, right_index)


def find_all_occurances(numbers, number_to_find):
    index = binary_search(numbers, number_to_find)
    indices = [index]
    # find indices on left hand side
    i = index-1
    while i >=0:
        if numbers[i] == number_to_find:
            indices.append(i)
        else:
            break
        i = i - 1

    # find indices on right hand side
    i = index + 1
    while i<len(numbers):
        if numbers[i] == number_to_find:
            indices.append(i)
        else:
            break
        i = i + 1

    return sorted(indices)

if __name__ == "__main__":
    num_list = [12, 15, 17, 19, 21, 24, 45, 67]
    target = 45

    result = linear_search(num_list, target)
    result2 = binary_search(num_list, target)
    result3 = binary_search(num_list, target)

    print(f"Target at index {result} using linear search")
    print(f"Target at index {result2} using binary search")
    print(f"Target at index {result3} using binary search")

    numbers = [1, 4, 6, 9, 11, 15, 15, 15, 17, 21, 34, 34, 56]
    number_to_find = 15

    solution = find_all_occurances(numbers, number_to_find)
    print(f"The 15's are located at {solution}")

# Binary Search Exercise
# When I try to find number 5 in below list using binary search, it doesn't work and returns me -1 index. Why is that?
#
# numbers = [1,4,6,9,10,5,7]
#
# Find index of all the occurances of a number from sorted list
#
# numbers = [1,4,6,9,11,15,15,15,17,21,34,34,56]
# number_to_find = 15
# This should return 5,6,7 as indices containing number 15 in the array

# Solutions

# It cannot find 5 because Binary search only works on sorted arrays

