a, b, c = map(int, input().split())
x = [5, 7]
if (a + b + c == 17) and (a in x) and (b in x) and (c in x):
    print('YES')
else:
    print('NO')