import math
a, b = map(int, input().split())

for i in range(1, 1001):
    if math.floor(i*0.08) == a and math.floor(i*0.10) == b:
        print(i)
        break
else:
    print('-1')