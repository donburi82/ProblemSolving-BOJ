import sys

def merge(a: list, l: int, m: int, r: int) -> int:
    global count, K

    nl = m-l+1
    n2 = r-m

    L = a[l:m+1]
    R = a[m+1:r+1]

    L.append(float('inf'))
    R.append(float('inf'))

    i, j = 0, 0
    for k in range(l, r+1):
        count += 1
        if L[i] <= R[j]:
            a[k] = L[i]
            i += 1
        else:
            a[k] = R[j]
            j += 1
        if count==K:
            print(a[k])
            break

    return 1

def mergeSort(a: list, l: int, r: int) -> int:
    if l < r:
        m = l+(r-l)//2 # same as (l+r)//2 but avoids overflow
        mergeSort(a, l, m)
        mergeSort(a, m+1, r)
        merge(a, l, m, r)
    return 1

n, K = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
count = 0
elem = -1
mergeSort(a, 0, n-1)
if count < K:
    print(-1)