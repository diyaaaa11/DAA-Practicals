# Iterative Factorial
def iterative(n):
    fact = 1

    for i in range(1, n + 1):
        fact = fact * i

    return fact


# Recursive Factorial
def recursive(n):
    if n == 0 or n == 1:
        return 1

    return n * recursive(n - 1)


# Input
n = int(input("Enter a number: "))

if n < 0:
    print("Factorial not possible")
else:
    print("Iterative:", iterative(n))
    print("Recursive:", recursive(n))

    print("Time Complexity of Iterative: O(n)")
    print("Time Complexity of Recursive: O(n)")