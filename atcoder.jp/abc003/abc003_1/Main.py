n = int(input())
ans = 0
for i in range(n):
    ans += 10000 * (i + 1)
print(int(ans / n))