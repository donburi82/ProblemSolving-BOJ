import sys

n, m = map(int, sys.stdin.readline().split())
nToNum = dict()
numToN = dict()
for i in range(1, n+1):
    name = sys.stdin.readline().strip()
    nToNum[name] = i
    numToN[i] = name
for _ in range(m):
    s = sys.stdin.readline().strip()
    try:
        num = int(s)
        print(numToN[num])
    except:
        print(nToNum[s])