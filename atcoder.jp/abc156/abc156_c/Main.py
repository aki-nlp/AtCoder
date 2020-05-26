n = int(input())
x = list(map(int, input().split()))

ans = 10 ** 9
for i in range(0, 101):
    s = 0
    for xx in x:
        s +=(i - xx) ** 2
    ans = min(ans, s)
print(ans)