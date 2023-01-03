import sys

s = sys.stdin.readline().strip()
a = [*s]
a = list(map(int,a))
print(''.join(list(map(str, sorted(a, key=lambda x: -x)))))