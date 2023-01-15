import sys

n = int(sys.stdin.readline())
d = dict()
for x in map(int, sys.stdin.readline().split()):
    if x in d.keys():
        d[x] += 1
    else:
        d[x] = 1
m = int(sys.stdin.readline())
for x in map(int, sys.stdin.readline().split()):
    if x in d.keys():
        print(d[x], end=' ')
    else:
        print(0, end=' ')