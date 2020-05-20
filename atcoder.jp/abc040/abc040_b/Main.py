n = int(input())

ans = 10**10
for i in range(1, n+1):
    j = n // i
    ans = min(ans, abs(j - i) + (n - i * j))
                      
print(ans)