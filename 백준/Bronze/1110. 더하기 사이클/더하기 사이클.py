import sys
n = sys.stdin.readline().strip()
a = n
count = 0
while True:
    if len(a) < 2:
        a = a*2
    else:
        temp = str(int(a[0])+int(a[1]))
        if len(temp) < 2:
            temp = '0'+temp
        a = a[1]+temp[1]
    count += 1
    if int(a)==int(n):
        break
print(count)