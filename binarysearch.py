# Binary Search Function
def binary_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid

        elif arr[mid] < key:
            low = mid + 1

        else:
            high = mid - 1

    return -1


# Get sorted numbers from the user
user_input = input("Enter sorted numbers separated by spaces: ")
arr = [int(num) for num in user_input.split()]

# Number to search
key = int(input("Enter the number to search: "))

# Call the function
result = binary_search(arr, key)

# Display result
if result != -1:
    print("Element found at index", result)
else:
    print("Element not found")