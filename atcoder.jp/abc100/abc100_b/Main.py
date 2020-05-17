d, n = map(int, input().split())
if n % 100 != 0:
    print((100 ** d) * n)
if n % 100 == 0:
    print((100 ** d) * (n+1))