import sys
from collections import Counter

# get info
k = int(sys.stdin.readline())
dire = []
length = []
dist = []
for _ in range(6):
    d, l = map(int, sys.stdin.readline().split())
    dire.append(d)
    length.append(l)
    dist.append((d, l))

# find width, height, and indices
a = []
for item in Counter(dire).items():
    if item[1]==1:
        a.append(item[0])
w, h = 0, 0
w_idx, h_idx = -1, -1
for x in a:
    dire.remove(x)
    for item in dist:
        if x==item[0]:
            w = item[1]
            w_idx = dist.index((x, w))
            if w > h:
                w, h = h, w
                w_idx, h_idx = h_idx, w_idx
            break
# find sub-rectangle
full = set([i for i in range(6)])
rem = set([(w_idx-1)%6, (w_idx)%6, (w_idx+1)%6, (h_idx-1)%6, (h_idx)%6, (h_idx+1)%6])
sub = 1
for idx in full-rem:
    sub *= length[idx]

# answer
print((w*h-sub)*k)