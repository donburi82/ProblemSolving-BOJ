import sys

largest = -1
idx = (-1, -1)
a = []
for _ in range(9):
    row = list(map(int, sys.stdin.readline().split()))
    a.append(row)
for i in range(9):
    for j in range(9):
        if a[i][j] > largest:
            largest = a[i][j]
            idx = (i+1, j+1)
print(largest)
print(*idx)