import sys

def dpFib(n):
    f = [0 for _ in range(n+1)]
    f[1], f[2] = 1, 1
    for i in range(3, n+1):
        f[i] = f[i-1]+f[i-2]
    return f[n]

n = int(sys.stdin.readline())
print(dpFib(n), n-2)