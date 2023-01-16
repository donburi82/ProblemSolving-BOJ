import sys

n, m = map(int, sys.stdin.readline().split())
d = set()
for _ in range(n):
    d.add(sys.stdin.readline().strip())
b = set()
for _ in range(n):
    b.add(sys.stdin.readline().strip())
db = sorted(list(d.intersection(b)))
print(len(db))
print(*db, sep="\n")