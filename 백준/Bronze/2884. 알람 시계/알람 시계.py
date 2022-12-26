import sys
H, M = map(int, sys.stdin.readline().split())
if M-45<0:
    H = (H-1)%24
    M = (M-45)%60
else:
    M -= 45
print(H, M)