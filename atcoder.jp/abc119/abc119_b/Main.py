n = int(input())
x = [list(input().split()) for _ in range(n)]
BTC = 380000.0
YEN = 1
ans = 0
for i in x:
    if i[1] =='BTC':
        ans += float(i[0]) * BTC
    else:
        ans += float(i[0]) * YEN
print(ans)