a = [int(input()) for _ in range(3)]
l = sorted(a, reverse=True)
print(l.index(a[0]) + 1)
print(l.index(a[1]) + 1)
print(l.index(a[2]) + 1)