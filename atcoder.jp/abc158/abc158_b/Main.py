n, a, b = map(int, input().split())
x = n  // (a + b) * a 
y = min(a, n - (n // (a + b)*(a + b)))
print(x + y)