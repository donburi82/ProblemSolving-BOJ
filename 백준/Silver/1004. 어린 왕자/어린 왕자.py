import sys

t = int(sys.stdin.readline())
for _ in range(t):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    n = int(sys.stdin.readline())
    s1 = set()
    s2 = set()
    for _ in range(n):
        cx, cy, r = map(int, sys.stdin.readline().split())
        if (x1-cx)**2 + (y1-cy)**2 <= r**2:
            s1.add((cx, cy, r))
        if (x2-cx)**2 + (y2-cy)**2 <= r**2:
            s2.add((cx, cy, r)) 
    print(len((s1|s2) - (s1&s2)))