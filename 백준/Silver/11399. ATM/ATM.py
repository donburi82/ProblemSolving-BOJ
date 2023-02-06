import sys

n = int(sys.stdin.readline())
ppl = list(map(int, sys.stdin.readline().split()))
ppl.sort()
total = 0
for person in ppl:
    total += person*n
    n -= 1
print(total)