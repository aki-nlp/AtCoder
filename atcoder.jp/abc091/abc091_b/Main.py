dic = {}

n = int(input())
for _ in range(n):
    s = input()
    if dic.get(s):
        dic[s] += 1
    else: 
        dic[s] = 1
        
m = int(input())
for _ in range(m):
    s = input()
    if dic.get(s):
        dic[s] -= 1
    else: 
        dic[s] = -1

ans = 0
for k, v in dic.items():
    ans = max(ans, v)
    
print(ans)

