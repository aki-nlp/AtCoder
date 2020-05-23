n, a, b = map(int, input().split())

ans = 0
for _ in range(n):
    s, d = input().split()
    d = int(d)
    if a <= d <= b:
        ans += d * ((s=='East')*2 -1)
    elif d < a:
        ans += a * ((s=='East')*2 -1)
    else:
        ans += b * ((s=='East')*2 -1)
        
if ans == 0:
    print(0)
elif ans > 0:
    print('East ' + str(ans))
else:
     print('West ' + str(-1 * ans))