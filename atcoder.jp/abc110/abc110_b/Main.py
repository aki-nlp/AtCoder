n, m, X, Y = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

x = max(x)
y = min(y)

flag = True
for z in range(-100, 100+1):
    if x < z <= y and X < z <= Y:
        flag = False
        
if flag:
    print('War')
else:
    print('No War')