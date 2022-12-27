import sys
s = set()
for _ in range(10):
    x = int(sys.stdin.readline())
    s.add(x%42)
print(len(s))