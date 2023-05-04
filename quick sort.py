def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quicksort(left) + middle + quicksort(right)

# example usage
my_array = [3, 6, 198, 10, 1, 2, 99]
sorted_array = quicksort(my_array)
print(sorted_array)
