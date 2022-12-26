import sys
x = int(sys.stdin.readline())
n = int(sys.stdin.readline())
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    x -= a*b
print("Yes" if x==0 else "No")