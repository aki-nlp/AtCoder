h, n = map(int, input().split())
a = list(map(int, input().split()))

if h - sum(a) <= 0:
    print('Yes')
else:
    print('No')