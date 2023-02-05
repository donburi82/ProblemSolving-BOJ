import sys

n, k = map(int, sys.stdin.readline().split())
denominations = []
for _ in range(n):
    denominations.append(int(sys.stdin.readline()))
count = 0
for coin in denominations[::-1]:
    count += k//coin
    k = k%coin
print(count)