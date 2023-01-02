import sys

a = []
n = 5
total = 0
for _ in range(n):
    x = int(sys.stdin.readline())
    total += x
    a.append(x)
a.sort()
print(total//n, a[n//2])