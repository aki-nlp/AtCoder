n, x = map(int, input().split())
a = list(map(int, input().split()))
b = format(x, 'b')
ans = 0
for i in range(len(str(b))):
    ans += a[i] * int(str(b)[len(b)-1-i])
print(ans)