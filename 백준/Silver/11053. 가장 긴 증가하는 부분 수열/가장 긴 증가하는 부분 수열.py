import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
lis = [1]*n
for i in range(1, n):
    longest = -1
    for j in range(i):
        if a[i]>a[j]:
            longest = max(longest, lis[j])
    if longest!=-1:
        lis[i] += longest
print(max(lis))