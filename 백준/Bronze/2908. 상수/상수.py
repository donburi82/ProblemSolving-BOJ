import sys

A, B = sys.stdin.readline().strip().split()
print(A[::-1] if int(A[::-1])>int(B[::-1]) else B[::-1])