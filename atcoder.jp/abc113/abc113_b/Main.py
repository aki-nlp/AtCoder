n = int(input())
t, a =map(int, input().split())
h = list(map(int, input().split()))

ans = 1
res = 10**10
for i in range(n):
    if abs(a - (t - h[i] * 0.006)) < res:
        res = abs(a - (t - h[i] * 0.006))
        ans = i + 1
print(ans)