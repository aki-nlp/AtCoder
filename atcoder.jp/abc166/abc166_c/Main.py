n, m = map(int, input().split())
h = list(map(int, input().split()))
ab = [list(map(int, input().split())) for _ in range(m)]

x = [set() for _ in range(n)]
for a, b in ab:
    x[a-1].add(b-1)
    x[b-1].add(a-1)
    
ans = 0
for i, xx in enumerate(x):
    for xxx in xx:
        if h[i] <= h[xxx]:
            break
    else:
        ans += 1
        
print(ans)