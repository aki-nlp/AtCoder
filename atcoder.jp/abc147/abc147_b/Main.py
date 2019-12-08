s=input()
a=s[::-1]
r=0
for i in range(int(len(s)/2)):
    if(s[i]!=a[i]):
        r+=1
print(r)