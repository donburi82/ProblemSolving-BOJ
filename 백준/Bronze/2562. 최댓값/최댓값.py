import sys
M = -1
n = 0
for i in range(1, 10):
    x = int(sys.stdin.readline())
    if x > M:
        M = x
        n = i
print(M)
print(n)