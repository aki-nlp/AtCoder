import math
n = int(input())
while True:
    if math.sqrt(n) % 1 == 0:
        print(n)
        break
    n -= 1