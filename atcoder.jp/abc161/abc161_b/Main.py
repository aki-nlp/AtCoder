import numpy as np

n, m = map(int, input().split())
a = np.array(list(map(int, input().split())) )

a = a / sum(a)
a = (a >= 1/(4*m))
if sum(a)>=m:
    print('Yes')
else:
    print('No')