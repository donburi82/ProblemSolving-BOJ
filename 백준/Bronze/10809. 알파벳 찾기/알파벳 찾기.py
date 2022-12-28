import sys

s = sys.stdin.readline().strip()
for i in range(97, 123): # a97, z122
    print(s.find(chr(i)), end=' ')