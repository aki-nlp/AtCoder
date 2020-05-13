a, b, k = map(int, input().split())
b = max(0, b - (k - a) * (k - a > 0))
a = max(0, a - k) 
print(a, b)