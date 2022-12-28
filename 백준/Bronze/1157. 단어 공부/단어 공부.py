import sys

s = sys.stdin.readline().strip().upper()
max_freq = {}
for c in s:
    if c in max_freq:
        max_freq[c] += 1
    else:
        max_freq[c] = 1
max_val = max(max_freq.values())
max_key = ''
count = 0
for key, val in max_freq.items():
    if val==max_val:
        max_key = key
        count += 1
print(max_key if count==1 else '?')