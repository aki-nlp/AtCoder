import math
a = []
mini = 9
flag = False
for i in range(5):
    x = int(input())
    if x%10==0:
        a.append(x)
    else:
        flag = True
        if x%10<mini :
            mini = x%10
        a.append(math.ceil(x/10)*10)

if flag:
    print(sum(a)-(10-mini))
else:
    print(sum(a))