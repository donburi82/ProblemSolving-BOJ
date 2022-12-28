import sys

t = int(sys.stdin.readline())
for _ in range(t):
    r, s = sys.stdin.readline().strip().split()
    r = int(r)
    p = ''
    for c in s:
        p += c*r
    print(p)