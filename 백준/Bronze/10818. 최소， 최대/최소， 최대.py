import sys
n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
print(min(A), max(A))