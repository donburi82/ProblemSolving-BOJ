import sys

n = int(sys.stdin.readline())
a = set()
for _ in range(n):
    a.add(sys.stdin.readline().strip())
a = list(a)
a.sort(key=lambda x: (len(x), x))
print(*a, sep='\n')