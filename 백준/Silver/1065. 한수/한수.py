import sys

def isAP(n: int) -> bool:
    digits = list(map(int, str(n).strip()))
    if len(digits)==1 or len(digits)==2:
        return True
    c = digits[1]-digits[0]
    for i in range(2, len(digits)):
        if digits[i]-digits[i-1]!=c:
            return False
    return True

N = int(sys.stdin.readline())
count = 0
for i in range(1, N+1):
    if isAP(i):
        count += 1
print(count)