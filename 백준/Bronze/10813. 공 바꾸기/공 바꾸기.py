import sys

n, m = map(int, sys.stdin.readline().split())
a = [i for i in range(1, n+1)]
for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    a[i-1], a[j-1] = a[j-1], a[i-1]
print(*a)