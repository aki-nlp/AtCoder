n = int(input())
s = input()

ans = 0
for i in range(0, n-2):
    if 'ABC' == s[i:i+3]:
        ans += 1
print(ans)