a, b, c = map(int, input().split())

for i in range(1, 100):
    if a*i % b == c:
        print('YES')
        break
else:
    print('NO')