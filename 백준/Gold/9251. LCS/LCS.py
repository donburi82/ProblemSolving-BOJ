import sys

x = sys.stdin.readline().strip()
y = sys.stdin.readline().strip()
m = len(x)
n = len(y)
lcs = [[None]*(n+1) for _ in range(m+1)]
for i in range(m+1):
    for j in range(n+1):
        if i==0 or j==0:
            lcs[i][j] = 0
        elif x[i-1]==y[j-1]:
            lcs[i][j] = lcs[i-1][j-1]+1
        else:
            lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])
print(lcs[m][n])