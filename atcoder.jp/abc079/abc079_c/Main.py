s=input()
n=len(s)
ans=''

for bit in range(1<<(n-1)):
    f=int(s[0])
    g=s[0]
    for i in range(n-1):
        if bit&(1<<i):
            f+=int(s[i+1])
            g+='+'+s[i+1]
        else:
            f-=int(s[i+1])
            g+='-'+s[i+1]
    if f==7:
        ans=g
    
print(ans+'=7')