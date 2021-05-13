def merge_sort(arr):
    if len(arr) <= 1:
        return

    mid = len(arr)//2

    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)

    merge_two_sorted_lists(left, right, arr)


def merge_two_sorted_lists(a, b, arr):
    len_a = len(a)
    len_b = len(b)

    i = j = k = 0

    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            arr[k] = a[i]
            i += 1
        else:
            arr[k] = b[j]
            j += 1
        k += 1

    while i < len_a:
        arr[k] = a[i]
        i += 1
        k += 1

    while j < len_b:
        arr[k] = b[j]
        j += 1
        k += 1


def merge_sort_key(arr, key):
    if len(arr) <= 1:
        return

    mid = len(arr)//2

    left = arr[:mid]
    right = arr[mid:]

    merge_sort_key(left, key)
    merge_sort_key(right, key)

    merge_two_sorted_lists_key(left, right, arr, key)


def merge_two_sorted_lists_key(a, b, arr, key):
    len_a = len(a)
    len_b = len(b)

    i = j = k = 0

    while i < len_a and j < len_b:
        if a[i][key] <= b[j][key]:
            arr[k] = a[i]
            i += 1
        else:
            arr[k] = b[j]
            j += 1
        k += 1

    while i < len_a:
        arr[k] = a[i]
        i += 1
        k += 1

    while j < len_b:
        arr[k] = b[j]
        j += 1
        k += 1


if __name__ == '__main__':
    test_cases = [
        [10, 3, 15, 7, 8, 23, 98, 29],
        [],
        [3],
        [9, 8, 7, 2],
        [1, 2, 3, 4, 5]
    ]

    for test in test_cases:
        merge_sort(test)
        print(test)

    elements = [
            {'name': 'rajab', 'age': 12, 'time_hours': 3},
            {'name': 'vignesh', 'age': 21, 'time_hours': 2.5},
            {'name': 'chinmay', 'age': 24, 'time_hours': 1.5},
            {'name': 'vedanth', 'age': 17, 'time_hours': 1},
    ]

    merge_sort_key(elements, 'name')
    print(elements)

    elements = [
            {'name': 'rajab', 'age': 12, 'time_hours': 3},
            {'name': 'vignesh', 'age': 21, 'time_hours': 2.5},
            {'name': 'chinmay', 'age': 24, 'time_hours': 1.5},
            {'name': 'vedanth', 'age': 17, 'time_hours': 1},
    ]

    merge_sort_key(elements, 'time_hours')
    print(elements)

# Merge Sort Exercise
# Modify merge_sort function such that it can sort following list of athletes as per the time
# taken by them in the marathon,
#
# elements = [
#         { 'name': 'vedanth',   'age': 17, 'time_hours': 1},
#         { 'name': 'rajab', 'age': 12,  'time_hours': 3},
#         { 'name': 'vignesh',  'age': 21,  'time_hours': 2.5},
#         { 'name': 'chinmay',  'age': 24,  'time_hours': 1.5},
#     ]
# merge_sort function should take key from an athlete's marathon log and sort the list as per that key. For example,
#
# merge_sort(elements, key='time_hours', descending=True)
# This will sort elements by time_hours and your sorted list will look like,
#
# elements = [
#         {'name': 'rajab', 'age': 12, 'time_hours': 3},
#         {'name': 'vignesh', 'age': 21, 'time_hours': 2.5},
#         {'name': 'chinmay', 'age': 24, 'time_hours': 1.5},
#         {'name': 'vedanth', 'age': 17, 'time_hours': 1},
#     ]
# But if you call it like this,
#
# merge_sort(elements, key='name')
# output will be,
#
# elements = [
#         { 'name': 'chinmay',   'age': 24, 'time_hours': 1.5},
#         { 'name': 'rajab', 'age': 12,  'time_hours': 3},
#         { 'name': 'vedanth',  'age': 17,  'time_hours': 1},
#         { 'name': 'vignesh',  'age': 21,  'time_hours': 2.5},
#     ]
# Solution