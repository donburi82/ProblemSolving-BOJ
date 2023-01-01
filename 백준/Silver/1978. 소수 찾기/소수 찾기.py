import sys

def isPrime(x: int) -> bool:
    if x < 2:
        return False
    for d in range(2, x):
        if x%d==0:
            return False
    return True

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
count = 0
for x in a:
    if isPrime(x):
        count += 1
print(count)