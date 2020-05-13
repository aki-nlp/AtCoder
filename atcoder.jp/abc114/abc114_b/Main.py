s = input()
ans = 10**8
for i in range(0, len(s)-2):
    ans = min(ans, abs(753 - int(s[i:i+3])))
print(ans)