import sys

n = int(sys.stdin.readline())
if n==1:
    print(1)
else:
    dp = [0 for _ in range(n+1)]
    dp[1], dp[2] = 1, 2
    for i in range(3, n+1):
        dp[i] = (dp[i-1]+dp[i-2])%15746
    print(dp[n])