import numpy as np

n, m, c = map(int, input().split())
b = np.array(list(map(int, input().split())))
a = np.array([list(map(int, input().split())) for _ in range(n)])
ab = a*b

ans = 0
for i in ab:
    if sum(i) + c > 0:
        ans += 1
        
print(ans)