import sys
import math

def count(x: int, factor: int) -> int:
    count = 0
    while x!=0:
        x = x//factor
        count += x
    return count

n, m = map(int, sys.stdin.readline().split())
print(min(count(n, 2)-count(m, 2)-count(n-m, 2), count(n, 5)-count(m, 5)-count(n-m, 5)))