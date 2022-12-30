import sys

t = int(sys.stdin.readline())
count = 0
for _ in range(t):
    s = sys.stdin.readline().strip()
    if len(s) < 3:
        count += 1
    else:
        visited = [s[0]]
        prev = s[0]
        group = True
        for i in range(1, len(s)):
            if s[i] in visited and prev!=s[i]:
                group = False
                break
            elif prev!=s[i]:
                visited.append(s[i])
            prev = s[i]
        if group:
            count += 1
print(count)