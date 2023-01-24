# 원과 원의 접점 개수
import sys

t = int(sys.stdin.readline())
for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
    dist = ((x1-x2)**2+(y1-y2)**2)**0.5
    if dist==0 and r1==r2:
        print(-1)
    elif abs(r1-r2)==dist or r1+r2==dist: # 내접, 외접
        print(1)
    elif abs(r1-r2) < dist < r1+r2:
        print(2)
    else:
        print(0)