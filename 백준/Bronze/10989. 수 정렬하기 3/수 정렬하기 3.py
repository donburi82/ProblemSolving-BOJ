import sys

n = int(sys.stdin.readline())
k = 10001
c = [0]*k # count of numbers == i where 1<=i<=k
for _ in range(n):
    c[int(sys.stdin.readline())] += 1

for i in range(1, k):
    if c[i] != 0:
        for j in range(c[i]):
            print(i)