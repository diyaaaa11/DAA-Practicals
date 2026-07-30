def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
user_input = input("Enter numbers separated by spaces: ")
data = [float(num) for num in user_input.split()]
print("Original data:", data)
insertion_sort(data)
print("Sorted array: ", data)
