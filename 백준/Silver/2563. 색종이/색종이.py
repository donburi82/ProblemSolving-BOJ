import sys

n = int(sys.stdin.readline())
a = [[0 for col in range(100)] for row in range(100)]
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    x -= 1
    y -= 1
    for i in range(x, x+10):
        for j in range(y, y+10):
            a[i][j] = 1
count = sum(row.count(1) for row in a)
print(count)