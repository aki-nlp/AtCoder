#ARC 029 A - 高橋君とお肉
n=int(input())
t=[int(input()) for _ in range(n)]

ans=0
mini=1<<(1<<5)
for bit in range(1<<n):
    a=0; b=0
    for i in range(n):
        if bit>>i & 1:
            a+=t[i]
        else:
            b+=t[i]
    if abs(a-b)<mini:
        mini=abs(a-b)
        ans=max(a, b)
print(ans)