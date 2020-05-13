import numpy as np
n = int(input())
a = np.array(list(map(int, input().split())))
print(1 / sum(1 / a))