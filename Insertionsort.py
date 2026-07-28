def insertion_sort(arr):
    n = len(arr)
    
    # Traverse from the second element up to the last element
    for i in range(1, n):
        key = arr[i]
        
        # Move elements of arr[0..i-1] that are greater than key
        # to one position ahead of their current position
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            
        # Place the key into its correct sorted position
        arr[j + 1] = key

# 1. Get numbers from the user
user_input = input("Enter numbers separated by spaces: ")
data = [float(num) for num in user_input.split()]

# 2. Sort and display the results
print("Original data:", data)
insertion_sort(data)
print("Sorted array: ", data)
