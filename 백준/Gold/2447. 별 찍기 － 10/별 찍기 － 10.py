import sys

def concatenate(p1: str, p2: str) -> str:
    a1 = p1.strip().split("\n")
    a2 = p2.strip().split("\n")
    res = ""
    for i in range(len(a1)):
        res += a1[i]+a2[i]
        res += "\n"
    return res

def to2D(a: list, k: int) -> list:
    return [a[i:i+k] for i in range(0, len(a), k)]

def generatePattern(n: int) -> str:
    if n==3:
        return "***\n* *\n***"
    else:
        k = n//3
        ps = generatePattern(k)
        temp = ['e'*k for i in range(k)]
        pe = "\n".join(temp)
        patterns = [ps if i!=4 else pe for i in range(9)]
        patterns = to2D(patterns, 3)
        res = ''
        for i in range(3): # loop through rows
            row = ''
            for j in range(3): # loop through columns
                if j==0:
                    row += patterns[i][j]
                else:
                    row = concatenate(row, patterns[i][j])
            res += row
        res = res.replace('e', ' ')
        return res

n = int(sys.stdin.readline())
print(generatePattern(n))