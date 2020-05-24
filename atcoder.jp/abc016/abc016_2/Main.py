a, b, c = map(int, input().split())

p = a + b
m = a - b
if p == m == c:
    print('?')
elif p == c:
    print('+')
elif m == c:
    print('-')   
else:
    print('!')