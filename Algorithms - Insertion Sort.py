def insertion_sort(elements):
    for i in range(1, len(elements)):
        anchor = elements[i]
        j = i - 1
        while anchor < elements[j] and j >= 0:
            elements[j+1] = elements[j]
            j -= 1
        elements[j+1] = anchor


def median(elements):
    length = len(elements)
    if length % 2 == 0:
        print('Elements: ', elements, "\nMedian: ", (elements[length//2] + elements[(length//2) - 1])/2, "\n\n")
    else:
        print('Elements: ', elements, "\nMedian: ", elements[length//2], '\n\n')

def insertion_sort_median(elements):
    for i in range(1, len(elements)):
        anchor = elements[i]
        j = i - 1
        while anchor < elements[j] and j >= 0:
            elements[j+1] = elements[j]
            j -= 1
        elements[j+1] = anchor

        median(elements[:i+1])


if __name__ == '__main__':
    elements = [11,9,29,7,2,15,28]
    print(elements)
    #
    tests = [
        [11,9,29,7,2,15,28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6]
    ]

    for elements in tests:
        insertion_sort(elements)
        print(f'sorted array: {elements}')

    elements = [11,9,29,7,2,15,28]
    insertion_sort_median(elements)


# Exercise: Insertion Sort
# Compute the running median of a sequence of numbers.
# That is, given a stream of numbers, print out the median of the list so far on each new element.
#
# Recall that the median of an even-numbered list is the average of the two middle numbers in a sorted list.
#
# For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:
#
# 2
# 1.5
# 2
# 3.5
# 2
# 2
# 2