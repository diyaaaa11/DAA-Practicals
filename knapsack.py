# 0/1 Knapsack using Dynamic Programming

n = int(input("Enter number of items: "))

weight = []
value = []

for i in range(n):
    weight.append(int(input("Enter weight: ")))
    value.append(int(input("Enter value: ")))

capacity = int(input("Enter capacity: "))

# DP table
dp = [[0] * (capacity + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for w in range(1, capacity + 1):

        if weight[i - 1] <= w:
            dp[i][w] = max(
                value[i - 1] + dp[i - 1][w - weight[i - 1]],
                dp[i - 1][w]
            )
        else:
            dp[i][w] = dp[i - 1][w]

print("Maximum value:", dp[n][capacity])