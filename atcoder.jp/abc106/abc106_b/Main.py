import numpy as np

n = int(input())
l = [0 for i in range(0, 201)]

for i in range(1, 201):
    for j in range(i, 201):
        if j/i == int(j/ i):
            l[j] += 1

l = np.array(l[1:n+1:2])>=8
print(sum(l))