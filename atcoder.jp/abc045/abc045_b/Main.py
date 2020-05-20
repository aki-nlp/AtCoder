s = []
for _ in range(3):
    x = input().replace('a', '0').replace('b', '1').replace('c', '2')
    s.append(str(x))
    
now = 0
while True:
    if len(s[now]) == 0:
        if now == 0:
            print('A')
        if now == 1:
            print('B')   
        if now == 2:
            print('C')
        break
        
    after = int(s[now][0])
    s[now] =  s[now][1:]
    now = after