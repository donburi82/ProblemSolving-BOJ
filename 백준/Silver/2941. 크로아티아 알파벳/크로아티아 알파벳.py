import sys

cro = ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']
s = sys.stdin.readline().strip()
count = 0
i = 0
while i < len(s):
    count += 1
    if s[i:i+2] in cro:
        i += 2
    elif s[i:i+3]=='dz=':
        i += 3
    else:
        i += 1 
print(count)