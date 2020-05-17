n = int(input())
a = [i*4 for i in range(n//4 + 1)]
b = [i*7 for i in range(n//7 + 1)]

c =set()
for i in a:
    for j in b:
        if i+j != 0 and i+j <=n:
            c.add(i+j)
            
if n in c:
    print('Yes')
else:
    print('No')