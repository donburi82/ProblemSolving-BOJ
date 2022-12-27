import sys
t = int(sys.stdin.readline())
for _ in range(t):
    A = list(map(int, sys.stdin.readline().split()))
    n = A[0]
    average = sum(A[1:])/n
    print("{:0.3f}%".format(sum(x > average for x in A[1:])*100/n))