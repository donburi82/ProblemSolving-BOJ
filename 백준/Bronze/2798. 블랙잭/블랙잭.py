import sys

n, m = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
total = -1
diff = 300000
for i in range(len(a)-2):
    for j in range(i+1, len(a)-1):
        for k in range(j+1, len(a)):
            temp = a[i]+a[j]+a[k]
            if temp <= m and abs(temp-m) < diff:
                total = temp
                diff = abs(temp-m)
print(total)