n = int(input())
p =  list(map(int, input().split()))

pre = p[0]
ans = 0
for i in p:
    if i <= pre:
        ans += 1
        pre = i    
print(ans)