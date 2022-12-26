import sys
x = int(sys.stdin.readline())
y = int(sys.stdin.readline())
if x<0:
    if y<0:
        print(3)
    elif y>0:
        print(2)
elif x>0:
    if y<0:
        print(4)
    elif y>0:
        print(1)