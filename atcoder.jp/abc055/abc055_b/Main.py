n = int(input())

ans = 1
for i in range(n):
    ans *= i + 1
    ans %= 10**9 + 7
print(ans)