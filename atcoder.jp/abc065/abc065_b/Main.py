n = int(input())
a= [int(input()) for _ in range(n)]

i = 1
ans = 0
while True:
    if a[i-1] == -1:
        print(-1)
        break
    ni = a[i-1]
    a[i-1] = -1
    i = ni
    ans +=1
    if i==2:
        print(ans)
        break