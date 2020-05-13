import numpy as np

a = np.array([list(map(int, input().split())) for _ in range(3)])
n = int(input())
b = [int(input()) for _ in range(n)]

for i in range(3):
    for j in range(3):
        if a[i][j] in b:
            a[i][j] = -1
            
flag = False
for i in a:
    if sum(i)==-3:
        flag = True
for i in a.T:
    if sum(i)==-3:
        flag = True
if a.trace() == -3 or  sum([a[0][2], a[1][1], a[2][0]]) == -3:
    flag = True
    
if flag:
    print('Yes')
else:
    print('No')