def shell_sort(arr):
    size = len(arr)
    gap = size//2

    while gap > 0:
        for i in range(gap, size):
            anchor = arr[i]
            j = i
            while j >= gap and arr[j-gap] > anchor:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = anchor
        gap = gap // 2


def shell_sort_remove_duplicates(arr):
    n = len(arr)
    div = 2
    gap = n//div
    while gap > 0:
        index_to_delete = []
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j-gap] >= temp:
                if arr[j-gap] == temp:
                    index_to_delete.append(j)
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = temp
        index_to_delete=list(set(index_to_delete))
        index_to_delete.sort()
        if index_to_delete:
            for i in index_to_delete[-1::-1]:
                del arr[i]
        div *= 2
        n = len(arr)
        gap = n//div


if __name__ == '__main__':
    tests = [
        [89, 78, 61, 53, 23, 21, 17, 12, 9, 7, 6, 2, 1],
        [],
        [1, 5, 8, 9],
        [234, 3, 1, 56, 34, 12, 9, 12, 1300],
        [5]
    ]

    for elements in tests:
        shell_sort(elements)
        print(elements)

    elements = [89, 89, 78, 61, 53, 23, 21, 17, 12, 9, 9, 7, 6, 2, 1]
    shell_sort_remove_duplicates(elements)
    print(elements)

# Exercise: Shell Sort
# Sort the elements of a given list using shell sort, but with a slight modification.
# Remove all the repeating occurances of elements while sorting.
#
# Traditionally, when comparing two elements in shell sort, we swap if first element is bigger than second,
# and do nothing otherwise.
#
# In this modified shell sort with duplicate removal, we will swap if first element is bigger than second,
# and do nothing if element is smaller,
# but if values are same, we will delete one of the two elements we are comparing before
# starting the next pass for the reduced gap.
#
# For example, given the unsorted list [2, 1, 5, 7, 2, 0, 5, 1, 2, 9, 5, 8, 3],
# after sorting using shell sort without duplicates, the sorted list would be:
#
# [0, 1, 2, 3, 5, 7, 8, 9]