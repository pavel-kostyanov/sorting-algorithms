from random import randrange, shuffle


def quick_sort(arr, start, end):
    if start >= end:
        return
    # pivot_index = randrange(start, end + 1)
    # pivot = arr[pivot_index]
    pivot_index = (end + start) // 2
    pivot = arr[pivot_index]
    lesser_than = start
    arr[pivot_index], arr[end] = arr[end], arr[pivot_index]

    for i in range(start, end):
        if arr[i] <= pivot:
            arr[i], arr[lesser_than] = arr[lesser_than], arr[i]
            lesser_than += 1

    arr[lesser_than], arr[end] = arr[end], arr[lesser_than]

    quick_sort(arr, lesser_than + 1, end)
    quick_sort(arr, start, lesser_than - 1)


unsort = [541, 22, 34, 5674, 24, 134, 84, 135, 5, 125, 456, 16, 7, 987, 1187, 47, 18, 69]

quick_sort(unsort, 0, len(unsort) - 1)
print(unsort)

"""
******* CODECADEMY VERSION OF QUICK-SORT **************
def quick_sort(arr, start, end):
    if start >= end:
        return
      # select random element to be pivot
    pivot_idx = randrange(start, end + 1)
    pivot_element = arr[pivot_idx]

     # swap random element with last element in sub-listay
    arr[end], arr[pivot_idx] = arr[pivot_idx], arr[end]

    less_than_pointer = start

    for i in range(start, end):
    # we found an element out of place
        if arr[i] < pivot_element:
    # swap element to the right-most portion of lesser elements
            arr[i], arr[less_than_pointer] = arr[less_than_pointer], arr[i]
            less_than_pointer += 1
    # move pivot element to the right-most portion of lesser elements
    arr[end], arr[less_than_pointer] =  arr[less_than_pointer], arr[end]
    # Call quicksort on the "left" and "right" sub-lists
    quick_sort(arr, start, less_than_pointer -1)
    quick_sort(arr, less_than_pointer + 1, end)

quick_sort(unsort, 0, len(unsort) - 1)
print(unsort)
"""
"""
******* MY OWN VERSION OF QUICK-SORT ***************
def quick_sort(arr):
    if len(arr) > 1:
        x = arr[0]
        left = [element for element in arr if element < x]
        mid = [element for element in arr if element == x]
        right = [element for element in arr if element > x]
        print(left, mid, right, sep = "\t")
        return quick_sort(left) + mid + quick_sort(right)
    else:
        return arr
"""


unsorted_list = [830, 921, 163, 373, 961, 559, 89, 199, 535, 959, 40, 641, 355, 689, 621, 183, 182, 524, 1]
