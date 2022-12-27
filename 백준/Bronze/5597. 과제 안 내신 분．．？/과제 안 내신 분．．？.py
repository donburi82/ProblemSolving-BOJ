import sys
A = [i for i in range(1, 31)]
for _ in range(28):
    s = int(sys.stdin.readline())
    A.remove(s)
print(A[0], A[1], sep='\n')