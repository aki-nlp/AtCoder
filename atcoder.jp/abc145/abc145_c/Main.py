import math
n=int(input())
x=[]
for _ in range(n):
    a,b=map(int, input().split())
    x.append([a,b])

l=0
for i in range(n):
    for j in range(n):
        l+=math.sqrt((x[i][0]-x[j][0])**2+(x[i][1]-x[j][1])**2)
print(l/n)