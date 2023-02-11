import sys

n, w = map(int, sys.stdin.readline().split())
wt = [0]
v = [0]
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    wt.append(a)
    v.append(b)
dp = [[0]*(w+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, w+1):
        if wt[i]<=j:
            dp[i][j] = max(v[i]+dp[i-1][j-wt[i]], dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]
print(dp[n][w])