import sys

x = int(sys.stdin.readline())
a = 0
d = 1
count = 0
while True:
    a += d
    d += 1
    count += 1
    if a >= x:
        break
n = a-x+1
print(f"{n}/{d-n}" if count%2==1 else f"{d-n}/{n}")