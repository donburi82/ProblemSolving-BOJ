import sys
n, x = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
for item in A:
    if item < x:
        print(item, end=" ")