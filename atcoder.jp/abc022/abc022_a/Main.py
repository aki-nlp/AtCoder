n ,s, t = map(int, input().split())
w = int(input())
a = [int(input()) for _ in range(n-1)]

ans = 0

weight = w
if s <= weight <= t:
        ans += 1
for i in a:
    weight += i
    if s <= weight <= t:
        ans += 1
print(ans)