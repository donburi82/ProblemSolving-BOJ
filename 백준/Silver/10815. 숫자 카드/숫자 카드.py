import sys

n = int(sys.stdin.readline())
own = set(map(int, sys.stdin.readline().split()))
t = int(sys.stdin.readline())
check = list(map(int, sys.stdin.readline().split()))
for i in range(t):
    if check[i] in own:
        print(1, end=' ')
    else:
        print(0, end=' ')