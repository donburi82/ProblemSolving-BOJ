import sys

n, m = map(int, sys.stdin.readline().split())
a = [i for i in range(1, n+1)]
for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    a = a[:i-1] + a[i-1:j][::-1] + a[j:]
print(*a)