import sys
from collections import Counter

n = int(sys.stdin.readline())
a = []
for _ in range(n):
    a.append(int(sys.stdin.readline()))
a.sort()
print(round(sum(a)/n))
print(a[n//2])
count = Counter(a).most_common(2)
if len(count) > 1:
    if count[0][1]==count[1][1]:
        print(count[1][0])
    else:
        print(count[0][0])
else:
    print(count[0][0])
print(max(a)-min(a))