n, t = map(int, input().split())
a = [int(input()) for _ in range(n)]

ans = t
for i in range(n-1):
    if a[-i-1] - a[-i-2] >= t:
        ans += t
    else:
        ans += a[-i-1] - a[-i-2]
print(ans)