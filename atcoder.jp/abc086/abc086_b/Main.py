import math

a, b = map(int, input().split())
c =int(str(a) + str(b))
if math.sqrt(c) % 1 == 0:
    print('Yes')
else:
    print('No')