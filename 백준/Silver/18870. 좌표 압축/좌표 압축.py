import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
b = sorted(set(a))
d = {b[i]: i for i in range(len(b))}
print(' '.join([str(d[x]) for x in a]))