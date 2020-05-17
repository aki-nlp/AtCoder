import numpy as np

h,w = map(int, input().split())
a = [list(input()) for _ in range(h)]

b = []
for i in a:
    if set(i) != {'.'}:
        b.append(i)
b = np.array(b)
b = b.T

c = []
for i in b:
    if set(i) != {'.'}:
        c.append(i)
c = np.array(c)
c = c.T

for i in c:
    print(''.join(i))