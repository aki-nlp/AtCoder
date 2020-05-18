n = int(input())
d, x = map(int, input().split())
day = [i for i in range(0, d+1)]

ans = 0
for _ in range(n):
    a = int(input())
    ans += len(day[1:d+1:a])
print(ans + x)