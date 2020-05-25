import math

def gcd(*numbers):
    return math.gcd( math.gcd(a, b), c)

k = int(input())

ans = 0
for a in range(1, k+1):
    for b in range(1, k+1):
        for c in range(1, k+1):
            ans += gcd(a, b, c)

print(ans)
            