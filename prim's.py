n = int(input("Enter number of vertices: "))

print("Enter adjacency matrix:")
cost = []
for i in range(n):
    cost.append(list(map(int, input().split())))

selected = [False] * n
selected[0] = True
total = 0

print("Minimum Spanning Tree:")

for _ in range(n - 1):
    minimum = float('inf')

    for i in range(n):
        if selected[i]:
            for j in range(n):
                if not selected[j] and cost[i][j] != 0:
                    if cost[i][j] < minimum:
                        minimum = cost[i][j]
                        x, y = i, j

    if minimum == float('inf'):
        print("Graph is not connected")
        exit()

    print(x, "-", y, ":", minimum)
    total += minimum
    selected[y] = True

print("Minimum cost =", total)