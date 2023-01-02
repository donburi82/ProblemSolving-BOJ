import sys

def isPrime(x: int) -> bool:
    if x < 2:
        return False
    for d in range(2, int(x**0.5)+1):
        if x%d==0:
            return False
    return True

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    a, b = n//2, n//2
    while a>0:
        if isPrime(a) and isPrime(b):
            print(a, b)
            break
        a -= 1
        b += 1