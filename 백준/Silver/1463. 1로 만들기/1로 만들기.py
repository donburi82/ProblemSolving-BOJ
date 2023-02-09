import sys

n = int(sys.stdin.readline())
dp = [0]*(n+1)
for i in range(n-1, 0, -1):
    triple = dp[i*3]+1 if i*3 <= n else float('inf')
    double = dp[i*2]+1 if i*2 <= n else float('inf')
    subt = dp[i+1]+1
    dp[i] = min(triple, double, subt)
print(dp[1])