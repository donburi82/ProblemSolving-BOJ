import sys

n, m = map(int, sys.stdin.readline().split())
own = set()
for _ in range(n):
    own.add(sys.stdin.readline().strip())
count = 0
for _ in range(m):
    if sys.stdin.readline().strip() in own:
        count += 1
print(count)