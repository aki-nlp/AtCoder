import bisect
n,m= map(int, input().split())
p=[0]
for _ in range(n):
    p.append(int(input()))
    
ans=0; pp=set();
for i in range(n+1):
    for j in range(n+1):
        if p[i]+p[j]<=m:
            pp.add(p[i]+p[j])
pp=sorted(pp)
for i in pp:
    ans=max(ans, i+pp[bisect.bisect_right(pp,m-i)-1])
print(ans)