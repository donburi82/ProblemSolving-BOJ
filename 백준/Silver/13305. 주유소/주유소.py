import sys

n = int(sys.stdin.readline())
dist = list(map(int, sys.stdin.readline().split()))
stations = list(map(int, sys.stdin.readline().split()))
total = 0
i = 0
while i < len(stations)-1:
    if stations[i] <= stations[i+1]:
        travel = dist[i]
        travel += dist[i+1] if i+1<len(stations)-1 else 0
        total += stations[i]*travel
        i += 2
    else:
        total += stations[i]*dist[i]
        i += 1
print(total)