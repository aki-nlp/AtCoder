n, m = map(int, input().split())

if n >=12:
    n -= 12
l = 30 * n + 0.5 * m
s = 6 * m

ans = min(abs(l-s), 360-abs(l-s))
print(ans)