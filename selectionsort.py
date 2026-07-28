def selection_sort(arr):
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n):
        # Assume the current position is the minimum
        min_idx = i
        
        # Find the actual minimum element in the remaining unsorted array
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
                
        # Swap the found minimum element with the first unsorted element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# 1. Get numbers from the user
user_input = input("Enter numbers separated by spaces: ")
data = [float(num) for num in user_input.split()]

# 2. Sort and display the results
print("Original data:", data)
selection_sort(data)
print("Sorted array: ", data)
