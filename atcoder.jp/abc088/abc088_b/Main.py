import numpy as np

n = int(input())
a = np.array(list(map(int, input().split()))) * (-1)
a.sort()
print(-1 * (sum(a[0::2]) - sum(a[1::2])))