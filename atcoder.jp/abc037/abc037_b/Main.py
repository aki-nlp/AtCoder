n, q = map(int, input().split())
lrt = [list(map(int, input().split())) for _ in range(q)]

a = [0] * n
for l, r, t in lrt:
    for i in range(l-1, r):
        a[i] = t
        
for i in a:
    print(i)