import sys

n, m = map(int, sys.stdin.readline().split())
a = []
b = []
result = [[0 for col in range(m)] for row in range(n)]
for _ in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    a.append(row)
for _ in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    b.append(row)
for i in range(n):
    for j in range(m):
        result[i][j] += a[i][j]+b[i][j]
for i in range(n):
    print(*result[i])