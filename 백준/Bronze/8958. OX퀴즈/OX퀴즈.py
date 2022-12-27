import sys
t = int(sys.stdin.readline())
for _ in range(t):
    s = sys.stdin.readline().strip()
    score = 0
    consecutive = 0
    for c in s:
        if c=="O":
            consecutive += 1
            score += consecutive
        else:
            consecutive = 0
    print(score)