import sys

n, k = map(int, sys.stdin.readline().split())
factorial = [1 for _ in range(n+1)]
for i in range(2, n+1):
    factorial[i] = factorial[i-1]*i
print((factorial[n]//(factorial[k]*factorial[n-k]))%10007)