n = int(input())
s = input()

x = 0
ans = 0
for i in s:
    if i == 'I':
        x += 1
        ans = max(ans, x)
    else:
        x -= 1
        
print(ans)