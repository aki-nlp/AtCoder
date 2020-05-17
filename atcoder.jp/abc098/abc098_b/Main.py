n = int(input())
s =input()
ans = 0
for i in range(n):
    a = set(s[0:i+1])
    b = set(s[i+1:])
    c = a & b
    ans = max(ans, len(c))
print(ans)