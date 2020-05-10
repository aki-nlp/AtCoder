import numpy as np
n, m, x = map(int,  input().split())
c=[]
a=[]
for _ in range(n):
    y = list(map(int, input().split()))
    c.append(y[0])
    a.append(y[1:])
    
def dfs(i, sum_c, sum_a):
    if i==n:
        if sum(sum_a>=x) == m:
            return sum_c
        else:
            return 10**12
    s1=dfs(i+1, sum_c+c[i], sum_a+np.array(a[i]))
    s2=dfs(i+1, sum_c, sum_a)
    return min(s1, s2)
  
ans=dfs(0, 0, np.array([0]*m))
if ans==10**12:
    print(-1)
else:
    print(ans)