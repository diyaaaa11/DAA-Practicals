def merge_sort(arr):
    # Base case: a list of 0 or 1 elements is already sorted
    if len(arr) <= 1:
        return arr

    # 1. Divide: Find the midpoint and split the array into two halves
    mid = len(arr) // quarter = len(arr) // 2
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursive calls to sort both halves
    merge_sort(left_half)
    merge_sort(right_half)

    # 2. Conquer: Merge the sorted halves back together
    i = j = k = 0

    # Copy data to temporary arrays left_half and right_half
    while i < len(left_half) and j < len(right_half):
        if left_half[i] <= right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        k += 1

    # Checking if any element was left in left_half
    while i < len(left_half):
        arr[k] = left_half[i]
        i += 1
        k += 1

    # Checking if any element was left in right_half
    while j < len(right_half):
        arr[k] = right_half[j]
        j += 1
        k += 1

# 1. Get numbers from the user
user_input = input("Enter numbers separated by spaces: ")
data = [float(num) for num in user_input.split()]

# 2. Sort and display the results
print("Original data:", data)
merge_sort(data)
print("Sorted array: ", data)
