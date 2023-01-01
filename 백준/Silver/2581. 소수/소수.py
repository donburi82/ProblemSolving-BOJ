import sys

def isPrime(x: int) -> bool:
    if x < 2:
        return False
    for d in range(2, x):
        if x%d==0:
            return False
    return True

m = int(sys.stdin.readline())
n = int(sys.stdin.readline())
primes = []
for x in range(m, n+1):
    if isPrime(x):
        primes.append(x)
if len(primes)==0:
    print(-1)
else:
    print(sum(primes))
    print(min(primes))