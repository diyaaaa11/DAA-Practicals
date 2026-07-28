def quick_sort(arr, low, high):
    if low < high:
        # Partition the array and get the pivot index
        pivot_index = partition(arr, low, high)
        
        # Recursively sort elements before and after partition
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    # Using the last element as the pivot
    pivot = arr[high]
    i = low - 1  # Index of smaller element
    
    for j in range(low, high):
        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            
    # Swap the pivot element with the greater element specified by i
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# 1. Get numbers from the user
user_input = input("Enter numbers separated by spaces: ")
data = [float(num) for num in user_input.split()]

# 2. Sort and display the results
print("Original data:", data)
quick_sort(data, 0, len(data) - 1)
print("Sorted array: ", data)
