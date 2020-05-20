n, m = map(int, input().split())
x = [list(map(int, input().split())) for _ in range(m)]

ans = [0] * n
for i in x:
    ans[i[0]-1] += 1
    ans[i[1]-1] += 1

for i in ans:
    print(i)