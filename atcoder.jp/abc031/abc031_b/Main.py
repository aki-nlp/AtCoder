l, h = map(int, input().split())
n = int(input())

for _ in range(n):
    a = int(input())
    if l <= a <= h:
        print(0)
    elif a > h:
        print(-1)
    else:
        print(l - a)