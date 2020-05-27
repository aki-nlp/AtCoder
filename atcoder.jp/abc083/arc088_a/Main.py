x, y = map(int, input().split())
n = 0
while True:
    if x * (2 ** n) <= y:
        n += 1
    else:
        break
print(n)