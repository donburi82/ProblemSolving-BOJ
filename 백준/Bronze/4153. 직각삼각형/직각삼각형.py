import sys

while True:
    l = list(map(int, sys.stdin.readline().split()))
    c = max(l)
    l.remove(c)
    if c==0:
        break
    if l[0]**2+l[1]**2==c**2:
        print("right")
    else:
        print("wrong")