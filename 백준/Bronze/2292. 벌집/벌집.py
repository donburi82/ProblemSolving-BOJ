import sys

n = int(sys.stdin.readline())
if n==1:
    print(1)
else:
    d = 6
    a = 1 
    while True:
        a += d
        d += 6
        if a >= n:
            print(d//6)
            break