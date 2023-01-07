import sys

def generateNum(n: int) -> int:
    return n+sum(map(int, str(n).strip()))

n = int(sys.stdin.readline())
for i in range(n):
    if generateNum(i)==n:
        print(i)
        exit()
print(0)