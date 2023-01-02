import sys

def insertionSort(a: list) -> int:
    n = len(a)
    for i in range(1, n):
        j = i-1
        while j>=0 and a[j]>a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            j -= 1
    return 1
    
n = int(sys.stdin.readline())
a = []
for _ in range(n):
    a.append(int(sys.stdin.readline()))
insertionSort(a)
print(*a, sep="\n")