def solve():
    a=-1;b=-1;c=-1
    n,Y=map(int, input().split())
    for x in range(n+1):
        for y in range(n+1):
            if 10000*x+5000*y+1000*(n-x-y)==Y and 0<=n-x-y<=n:
                a,b,c= [x,y,n-x-y]
    return a,b,c

a,b,c=solve()
print(a,b,c)