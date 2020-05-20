n, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]
cd = [list(map(int, input().split())) for _ in range(m)]

for x1, y1 in ab:
    l = 10**10
    index = 0
    for i, (x2, y2) in enumerate(cd):
        if l > abs(x1-x2)+abs(y1-y2):
            l = abs(x1-x2)+abs(y1-y2)
            index = i + 1
    print(index)