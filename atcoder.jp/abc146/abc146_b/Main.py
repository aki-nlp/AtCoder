n=int(input())
s=input()
s=list(s)
for i in range(len(s)):
    a=ord(s[i])+n
    if a>90:
        a-=26
    s[i]=chr(a)
print(''.join(s), end='')