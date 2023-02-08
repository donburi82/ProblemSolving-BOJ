import sys

dp = [0]*101
dp[1], dp[2], dp[3] = 1, 1, 1
for i in range(4, 101):
    dp[i] = dp[i-2]+dp[i-3]

t = int(sys.stdin.readline())
for _ in range(t):
    print(dp[int(sys.stdin.readline())])