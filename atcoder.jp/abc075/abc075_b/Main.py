h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]

def check(y, x):
    dx = [1, 0, -1]
    dy = [1, 0, -1]
    for i in dy:
        for j in dx:
            nx = x + j
            ny = y + i
            if 0<=nx<w and 0<=ny<h:
                if  s[ny][nx] == '#':
                    s[y][x] += 1

for i in range(h):
    for j in range(w):
        if s[i][j] == '.':
            s[i][j] = 0
            check(i, j)

for i in s:
    print(''.join(map(str, i)))