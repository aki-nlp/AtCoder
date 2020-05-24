n = int(input())
a = set()

for _ in range(n):
    a.add(int(input()))

a = sorted(a, reverse=True)
print(a[1])