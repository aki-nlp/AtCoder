import numpy as np
n = int(input())
a = np.array(list(map(int, input().split())))

b = np.argsort(a)
for i in b:
    print(i + 1, end=' ')
print()