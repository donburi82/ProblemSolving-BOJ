import sys
import math

n = int(sys.stdin.readline())
radii = list(map(int, sys.stdin.readline().split()))
base = radii[0]
for i in range(1, n):
    gcd = math.gcd(base, radii[i])
    print(f"{base//gcd}/{radii[i]//gcd}")