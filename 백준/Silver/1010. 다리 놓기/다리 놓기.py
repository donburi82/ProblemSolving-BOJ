import sys
import math

def nCr(n, r):
    f = math.factorial
    return f(n) // f(r) // f(n-r)

r, c = 30, 30
dp = [ [0 for _ in range(c)] for _ in range(r) ]
for n in range(1, r):
    for m in range(n, c):
        larger = n if n>m else m
        smaller = m if n>m else n
        dp[n][m] = nCr(larger, smaller)

t = int(sys.stdin.readline())
for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    print(dp[n][m])