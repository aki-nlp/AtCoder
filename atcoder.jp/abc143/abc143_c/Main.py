n = int(input())
s = input()

pre = s[0]
ans = 1
for i in s:
    if i != pre:
        ans +=1
        pre = i

print(ans)