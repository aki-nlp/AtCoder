a, b, c = map(int, input().split())
m = max(a, b, c)
print(m*10+(a+b+c-m))