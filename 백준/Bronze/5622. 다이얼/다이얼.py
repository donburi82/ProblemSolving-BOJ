import sys

dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
s = sys.stdin.readline().strip().upper()
t = 0
for c in s:
    for i in range(len(dial)):
        if c in dial[i]:
            t += i+3
print(t)