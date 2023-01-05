import sys

def towerOfHanoi(n: int, source, destination, mid):
    global count, result
    count += 1
    if n==1:
        # print(f"Move disk 1 from Rod {source} to Rod {destination}")
        result.append((source, destination))
        return
    else:
        towerOfHanoi(n-1, source, mid, destination) # move top n-1 disks to mid
        # print(f"Move disk {n} from Rod {source} to Rod {destination}") # move bottom disk to destination
        result.append((source, destination))
        towerOfHanoi(n-1, mid, destination, source) # move top n-1 disks to destination (from mid)

n = int(sys.stdin.readline())
count = 0
result = []
towerOfHanoi(n, 1, 3, 2)
print(count)
for x in result:
    print(*x)