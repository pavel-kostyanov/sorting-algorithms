unsort = [541, 22, 34, 5674, 24, 134, 84, 135, 5, 125, 456, 16, 7, 987, 1187, 47, 18, 69]

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


quick_sort(unsorted_list)






unsorted_list = [830, 921, 163, 373, 961, 559, 89, 199, 535, 959, 40, 641, 355, 689, 621, 183, 182, 524, 1]
