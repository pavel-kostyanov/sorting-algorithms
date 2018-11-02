def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    middle_index = len(arr) // 2
    left_side = arr[: middle_index]
    right_side = arr[middle_index :]

    left_sorted = merge_sort(left_side)
    right_sorted = merge_sort(right_side)

    return merge(left_sorted, right_sorted)

def merge(left, right):
    result = []

    while (left and right):
        if left[0] < right[0]:
            result.append(left[0])
            left.pop(0)
        else:
            result.append(right[0])
            right.pop(0)

    if left:
        result += left
    if right:
        result += right

    return result

unsorted_list = [830, 921, 163, 373, 961, 559, 89, 199]
sorted_list = merge_sort(unsorted_list)
print(sorted_list)
