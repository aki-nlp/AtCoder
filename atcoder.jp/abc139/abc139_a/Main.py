s = input()
t = input()

ans = 0
for a, b in zip(s, t):
    if a==b:
        ans += 1
print(ans)    