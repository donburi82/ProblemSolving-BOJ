import sys

n = int(sys.stdin.readline())
a = []
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    a.append((x, y))
for item in a:
    rank = 1
    for compare in a:
        if item[0]<compare[0] and item[1]<compare[1]:
            rank += 1 
    print(rank, end=' ')