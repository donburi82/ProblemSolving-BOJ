import sys

n = int(sys.stdin.readline())
a = []
for _ in range(n):
    age, name = sys.stdin.readline().split()
    age = int(age)
    a.append((age, name))
a.sort(key=lambda x: x[0])
for p in a:
    print(p[0], p[1])