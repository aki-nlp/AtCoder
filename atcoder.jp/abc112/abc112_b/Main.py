n, T = map(int, input().split())
ans = 10**10
for i in range(n):
    c, t = map(int, input().split())
    if t<=T:
        ans = min(ans, c)
if ans == 10**10:
    print('TLE')
else:
    print(ans)