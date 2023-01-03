import sys

n = int(sys.stdin.readline())
a = []
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    a.append((x, y))
a = sorted(a, key=lambda x: (x[1], x[0]))
for p in a:
    print(*p)