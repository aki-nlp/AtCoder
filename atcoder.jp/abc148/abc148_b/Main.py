n = int(input())
s, t = input().split()
for a, b in zip(s, t):
    print(a+b, end='')
print()