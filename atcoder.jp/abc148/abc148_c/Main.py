import fractions

def lcm(x, y):
    return (x * y) // fractions.gcd(x, y)

a, b = map(int, input().split())
print(lcm(a, b))