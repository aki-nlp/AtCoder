n, k, m = map(int, input().split())
a = list(map(int, input().split()))
s = sum(a)
if m * n - s <= k:
    print(max(0, m * n - s))
else:
    print(-1)