n, k = map(int, input().split())
ans = 1
while k <= n:
    n /= k
    ans += 1
print(ans)