import sys
import math

n = int(sys.stdin.readline())
fact = str(math.factorial(n))
count = 0
for c in fact[::-1]:
    if c!='0':
        break
    count += 1
print(count)