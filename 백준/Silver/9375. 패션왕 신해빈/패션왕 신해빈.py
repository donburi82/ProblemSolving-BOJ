import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    d = {}
    for _ in range(n):
        item, category = sys.stdin.readline().strip().split()
        if category not in d.keys():
            d[category] = set()
        d[category].add(item)
    count = 1
    # 종류마다 len+1: 입지 않는 경우를 포함
    for category in d.keys():
        count *= len(d[category])+1
    # 아무 의류도 안입는 경우를 소거
    print(count-1)