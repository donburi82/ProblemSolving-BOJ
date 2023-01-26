import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
if len(a)==1:
    print(a[0]**2)
else:
    a.sort()
    print(a[0]*a[-1])