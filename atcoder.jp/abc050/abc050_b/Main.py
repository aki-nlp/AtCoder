n = int(input())
t = list(map(int, input().split()))
m = int(input())
px = [list(map(int, input().split())) for _ in range(m)]

sum_t = sum(t)
for i in range(m):
    print(sum_t - t[px[i][0] - 1] +  px[i][1])