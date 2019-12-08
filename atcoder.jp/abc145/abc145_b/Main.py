n=int(input())
s=input()
a=s[0:int(n/2)]
b=s[int(n/2):]
if(a==b):
    print('Yes')
else:
    print('No')