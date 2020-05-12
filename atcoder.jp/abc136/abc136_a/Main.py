a, b, c = map(int, input().split())
ans = c - (a - b)
if ans > 0:
    print(ans)
else:
    print(0)