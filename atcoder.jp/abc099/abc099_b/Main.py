a, b = map(int, input().split())
x = [i  *(i + 1) // 2 for i in range(1, 1000)]
for i in range(999):
    if a <  x[i] and x[i] - a == x[i+1] - b:
        print(x[i] - a)
        break
