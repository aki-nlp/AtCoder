w, h, n = map(int, input().split())
xya = [list(map(int, input().split())) for _ in range(n)]

w1 = 0
w2 = w
h1 = 0
h2 = h
for x, y, a in xya:
    if a == 1:
        w1= max(w1, x)
    if a == 2:
        w2 = min(w2, x)
    if a == 3:
        h1 = max(h1, y)
    if a == 4:
        h2 = min(h2, y)
        
print(max(0, (w2-w1))*max(0, (h2-h1)))