a,b,c,k=map(int, input().split())
ans=0
if a>=k:
    ans+=k*1
    k=0
else:
    ans+=a*1
    k=k-a
if b>=k:
    ans+=k*0
    k=0
else:
    ans+=b*0
    k=k-b
if c>=k:
    ans+=k*-1
    k=0
else:
    ans+=c*-1
    k=k-c
print(ans)