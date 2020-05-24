n = int(input())
a = [0, 0, 1]
ans = 0
for _ in range(3, n):
    ans = (a[0]+a[1]+a[2]) % 10007
    a[0] = a[1]
    a[1] = a[2]
    a[2] = ans
if n == 3:
    print(1)
else:
    print(ans)