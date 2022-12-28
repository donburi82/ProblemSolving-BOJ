def d(n: int) -> int:
    return n+sum(list(map(int, str(n).strip())))

numbers = set(range(1, 10001))
toRemove = set()
for i in range(1, 10001):
    toRemove.add(d(i))
for num in sorted(numbers-toRemove):
    print(num)