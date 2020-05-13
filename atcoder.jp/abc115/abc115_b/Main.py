n = int(input())
p = [int(input()) for _ in range(n)]
m = max(p)
print(m // 2 + sum(p) - m)