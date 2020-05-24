n = int(input())
a = list(map(int, input().split()))

ans = 0
for i in a:
    x = i
    while not(x % 3 != 2 and x % 2 == 1):
        ans += 1
        x -= 1
print(ans)