# Matrix Chain Multiplication

n = int(input("Enter number of matrices: "))

# Take matrix dimensions from user
p = []

print("Enter dimensions of matrices:")

for i in range(n + 1):
    p.append(int(input(f"p[{i}] = ")))

# Create DP table
dp = [[0] * n for _ in range(n)]

# Calculate minimum multiplication cost
for length in range(2, n + 1):

    for i in range(n - length + 1):

        j = i + length - 1

        dp[i][j] = float('inf')

        for k in range(i, j):

            cost = (
                dp[i][k]
                + dp[k + 1][j]
                + p[i] * p[k + 1] * p[j + 1]
            )

            if cost < dp[i][j]:
                dp[i][j] = cost

# Display answer
print("\nMinimum number of scalar multiplications:",
      dp[0][n - 1])
    ++++