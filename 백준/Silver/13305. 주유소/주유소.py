import sys

n = int(sys.stdin.readline())
dists = list(map(int, sys.stdin.readline().split()))
costs = list(map(int, sys.stdin.readline().split()))
total = dists[0]*costs[0]
min_cost = costs[0]
for i in range(1, len(dists)):
    min_cost = min(min_cost, costs[i])
    total += min_cost*dists[i]
print(total)
