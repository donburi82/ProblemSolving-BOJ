import sys
H, M = map(int, sys.stdin.readline().split())
A = int(sys.stdin.readline())
if M+A < 60:
    M += A
else:
    H = (H+(M+A)//60)%24
    M = (M+A)%60
print(H, M)