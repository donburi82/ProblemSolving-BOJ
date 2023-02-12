import sys

def binarySearch(arr: list, low: int, high: int, x: int) -> int:
    if high>=low:
        mid = (low+high)//2
        if arr[mid]==x:
            return 1 # usually return index
        elif arr[mid]>x:
            return binarySearch(arr, low, mid-1, x)
        else:
            return binarySearch(arr, mid+1, high, x)
    else:
        return 0 # usually return -1

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
search = list(map(int, sys.stdin.readline().split()))
a.sort()
for i in range(m):
    print(binarySearch(a, 0, len(a)-1, search[i]))