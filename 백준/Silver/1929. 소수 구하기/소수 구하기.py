import sys

def eratosthenes(n: int, m: int = 2) -> list:
    sieve = [False, False] + [True]*(n-1)
    for i in range(2, int(n**0.5)+1):
        if sieve[i]==True:
            for j in range(2*i, n+1, i):
                sieve[j] = False
    return [i for i in range(m, n+1) if sieve[i]==True]

m, n = map(int, sys.stdin.readline().split())
primes = eratosthenes(n, m)
print(*primes, sep="\n")