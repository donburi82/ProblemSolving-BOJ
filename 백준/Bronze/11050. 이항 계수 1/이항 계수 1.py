import sys
import math

n, k = map(int, sys.stdin.readline().split())
print(math.factorial(n)//(math.factorial(k)*math.factorial(n-k)))