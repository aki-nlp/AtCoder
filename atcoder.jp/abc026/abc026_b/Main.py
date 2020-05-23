import math
n = int(input())
r= [int(input()) for _ in range(n)]

r = sorted(r)
ans = 0
for i in range(n):
    ans += r[i] * r[i] * ((-1) ** (i % 2))
print(abs(ans * math.pi))