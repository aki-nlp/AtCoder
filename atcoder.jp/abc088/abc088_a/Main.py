n = int(input())
a = int(input())

if a >= n - (n // 500) * 500:
    print('Yes')
else:
    print('No')