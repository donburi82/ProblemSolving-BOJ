import sys
n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
M = max(A)
new = [x/M*100 for x in A]
print(sum(new)/n)