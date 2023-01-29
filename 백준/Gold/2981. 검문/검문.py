import sys

def gcd(a: int, b: int) -> int:
    while b>0:
        a, b = b, a%b
    return a

n = int(sys.stdin.readline())
nums = []
for _ in range(n):
    nums.append(int(sys.stdin.readline()))
nums.sort()
diffs = []
for i in range(1, len(nums)):
    diffs.append(nums[i]-nums[i-1])
# gcd of diffs gives "M"
divisor = diffs[0]
for i in range(1, len(diffs)):
    divisor = gcd(divisor, diffs[i])
# divisors of M is the answer
m = []
for i in range(1, int(divisor**0.5)+1):
    if divisor%i==0:
        m.append(i)
        m.append(divisor//i)
m.remove(1)
print(*sorted(set(m)))