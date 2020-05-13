s = [list(map(int, input().split())) for _ in range(3)]
ans = 0
for i in s:
    ans += i[0]*i[1]//10
print(ans)