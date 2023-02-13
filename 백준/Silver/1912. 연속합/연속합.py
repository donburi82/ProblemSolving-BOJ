import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
v = [0]*n
v[0] = a[0]
largest = v[0]
for i in range(1, n):
    v[i] = v[i-1]+a[i]
    if v[i]<a[i]:
        v[i] = a[i]
    if v[i]>largest:
        largest = v[i]
print(largest)