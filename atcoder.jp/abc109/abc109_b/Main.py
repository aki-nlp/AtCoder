n = int(input())
w = [input() for _ in range(n)]

flag = True

before = w[0][0]
for i in w:
    if before != i[0]:
        flag = False
    before = i[-1]
    
if len(set(w))!=n:
    flag = False
    
if flag:
    print('Yes')
else:
    print('No')