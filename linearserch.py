# Function for Linear Search
def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i      # Return index if found
    return -1             # Return -1 if not found
r
user_input = input("Enter numbers separated by spaces: ")
arr = [int(num) for num in user_input.split()]

key = int(input("Enter the number to search: "))

result = linear_search(arr, key)

if result != -1:
    print("Element found at index", result)
else:
    print("Element not found")