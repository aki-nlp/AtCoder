n, m = map(int, input().split())
a = [set(input().split()[1:]) for _ in range(n)]

like = a[0]
for i in range(1, n):
    like = like & a[i]
print(len(like))