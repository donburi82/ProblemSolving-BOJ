import sys

s = set()
string = sys.stdin.readline().strip()
n = len(string)
for length in range(1, n+1): # 1 ~ n
    for j in range(0, n-length+1):
        s.add(string[j:j+length])
print(len(s))