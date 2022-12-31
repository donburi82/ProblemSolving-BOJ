import sys

n = int(sys.stdin.readline())
dp = [[-1 for col in range(n+1)] for row in range(2)]
# min no. of bags needed to create weight j using {3}
for j in range(n+1):
    if j%3==0:
        dp[0][j] = j//3
# min no. of bags needed to create weight j using {3, 5}
for j in range(n+1):
    dp[1][j] = dp[0][j]
    if j%5==0:
        dp[1][j] = j//5
    else:
        for i in range(j//5, -1, -1):
            remaining = j-5*i
            if remaining%3==0:
                dp[1][j] = i + dp[0][remaining]
                break
print(dp[1][n])