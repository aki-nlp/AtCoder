s = input()
rs= s[::-1]
a = s[:(len(s))//2]
ra = a[::-1]
b = s[(len(s)+2)//2:]
rb = a[::-1]

if s==rs and a==ra and b==rb:
    print('Yes')
else:
    print('No')