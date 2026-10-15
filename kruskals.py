n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

edges = []
print("Enter edges (u v weight):")

for i in range(e):
    u, v, w = map(int, input().split())
    edges.append((w, u, v))

edges.sort()
parent = list(range(n))
total = 0

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

print("Minimum Spanning Tree:")

for w, u, v in edges:
    a = find(u)
    b = find(v)

    if a != b:
        print(u, "-", v, ":", w)
        parent[a] = b
        total += w

print("Minimum cost =", total)