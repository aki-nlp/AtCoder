s = input()
t = int(input())

def move(x, y, s):
    if s == 'L':
        x = x - 1
    if s == 'R':
        x = x + 1
    if s == 'U':
        y = y + 1
    if s == 'D':
        y = y - 1
    return x, y

x = 0
y = 0
for i in s:
    x, y = move(x, y, i)


if t == 1:
    print(abs(x)+abs(y)+s.count('?'))
else:
    print(max(len(s)%2, abs(x)+abs(y)-s.count('?')))