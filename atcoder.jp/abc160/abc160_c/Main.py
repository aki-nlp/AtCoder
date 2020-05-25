k, n = map(int, input().split())
a = list(map(int, input().split()))
a.append(a[0] + k)
m = []
for i in range(n):
    m.append(a[i+1] - a[i])
print(k - max(m))