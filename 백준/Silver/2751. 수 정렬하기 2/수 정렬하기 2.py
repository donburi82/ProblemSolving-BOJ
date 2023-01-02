import sys

def merge(a: list, l: int, m: int, r: int) -> int:
    nl = m-l+1
    n2 = r-m

    L = a[l:m+1]
    R = a[m+1:r+1]

    L.append(float('inf'))
    R.append(float('inf'))

    i, j = 0, 0
    for k in range(l, r+1):
        if L[i] <= R[j]:
            a[k] = L[i]
            i += 1
        else:
            a[k] = R[j]
            j += 1

    return 1

def mergeSort(a: list, l: int, r: int) -> int:
    if l < r:
        m = l+(r-l)//2 # same as (l+r)//2 but avoids overflow
        mergeSort(a, l, m)
        mergeSort(a, m+1, r)
        merge(a, l, m, r)
    return 1

n = int(sys.stdin.readline())
a = []
for _ in range(n):
    a.append(int(sys.stdin.readline()))
mergeSort(a, 0, n-1)
print(*a, sep="\n")