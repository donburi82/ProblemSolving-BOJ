import sys

def recursion(s: str, l: int, r: int, depth: int):
    if l >= r:
        return (1, depth)
    elif s[l] != s[r]:
        return (0, depth)
    else:
        return recursion(s, l+1, r-1, depth+1)

def isPalindrome(s: str) -> int:
    return recursion(s, 0, len(s)-1, 1)

t = int(sys.stdin.readline())
for _ in range(t):
    s = sys.stdin.readline().strip()
    print(*isPalindrome(s))