import sys

n = int(sys.stdin.readline())
intervals = []
for _ in range(n):
    s, e = map(int, sys.stdin.readline().split())
    intervals.append((s, e))
intervals.sort(key=lambda x: (x[1], x[0]))
count = 0
prev = 0
for interval in intervals:
    if interval[0] >= prev:
        count += 1
        prev = interval[1]
print(count)